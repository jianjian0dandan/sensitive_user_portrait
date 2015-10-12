function call_ajax_request(url, callback){
    $.ajax({
      url: url,
      type: 'get',
      dataType: 'json',
      async: false,
      success:callback
    });
}

function Draw_resultTable(data){
    console.log(data);
    $('#group_task').empty();
	var item = data;
	var html = '';
	html += '<table class="table table-bordered table-striped table-condensed datatable" >';
	html += '<thead><tr style="text-align:center;">	<th>群组名称</th><th>时间</th><th>群组人数</th><th>备注</th><th>计算状态</th><th>操作</th></tr></thead>';
	html += '<tbody>';
	for (i=0;i<item.length;i++){
		html += '<tr>';
		for(j=0;j<item[i].length-1;j++){
			if (j==0){
				html += '<td name="task_name">'+item[i][j]+'</td>';
			}else{
				html += '<td>'+item[i][j]+'</td>';
			}
		}
		if(item[i][4]==1){
			html += '<td><a style="cursor:hand;" href="/index/group_analysis/?name=' + item[i][0]+ '">已完成</a></td>';
		}else{
			html += '<td>正在计算</td>';
		}
		html +='<td><a href="javascript:void(0)" id="del">删除</a></td>';
		html += '</tr>';
	}
	html += '</tbody>';
    html += '</table>';
	$('#group_task').append(html);

    deleteGroup();
   
}
function self_refresh(){
    window.location.reload();
}
function deleteGroup(){
	$('a[id^="del"]').click(function(e){
		var url = "/tag/delete_attribute/?";
		var temp = $(this).parent().prev().prev().prev().prev().prev().html();
		url = url + 'task_name=' + temp;
		console.log(url);
		//window.location.href = url;
		call_ajax_request(url,self_refresh);
	});
}
function page_init(){
    $('.datatable').dataTable({
        "sDom": "<'row'<'col-md-6'l ><'col-md-6'f>r>t<'row'<'col-md-12'i><'col-md-12 center-block'p>>",
        "sPaginationType": "bootstrap",
        "oLanguage": {
            "sLengthMenu": "_MENU_ 每页"
        }
    });
}
var url = '/group/show_task/'; 
call_ajax_request(url, Draw_resultTable);
bindButtonClick();


function bindButtonClick(){
	$("#search_all").click(function(){
        window.location.reload();
    });
    $('#searchbtn').off("click").click(function(){
        var url = "/group/show_task/?";
        console.log('clicked');
		url += get_input_data();
		call_ajax_request(url, Draw_resultTable);
        page_init();
        $("#search_group").modal("hide");
	});
}
//上传文件
function handleFileSelect(evt){
    var files = evt;
	var task_name = $('#file_task_name').val();
	var state = $('#file_state').val();
    for(var i=0,f;f=files[i];i++){
        var reader = new FileReader();
        reader.onload = function (oFREvent) {
			var a = oFREvent.target.result;	
			console.log(a);
			$.ajax({   
				type:"POST",  
				url:"/group/upload_file/",
				dataType: "json",
				async:false,
				data:{upload_data:a,task_name:task_name,state:state},
					
				success: function(){
					var show_url = "/group/show_task/";
					Group_result.call_sync_ajax_request(show_url,Group_result.ajax_method,Group_result.Draw_resultTable);
				}
					
			});
			location.reload();
		};            
		reader.readAsText(f,'GB2312');                                                        
    }
}
function get_input_data(){
	var temp='';
    var input_value;
    var input_name;
	 $('.searchinput').each(function(){
        input_name = $(this).attr('name')+'=';
        input_value = $(this).val()+'&';
        temp += input_name;
        temp += input_value;;
    });
	temp = temp.substring(0, temp.length-1);
	return temp;
}


