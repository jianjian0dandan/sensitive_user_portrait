# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from global_utils import ES_COPY_USER_PORTRAIT as es

index_info = {
    "settings":{
        "analysis":{
            "analyzer":{
                "my_analyzer":{
                    "type": "pattern",
                    "pattern": "&"
                }
            }
        }
    },

    "mappings":{
        "activeness":{
            "properties":{
                "uid":{
                    "type": "string",
                    "index": "not_analyzed"
                },
                "activeness_week_ave": {
                    "type": "double"
                },
                "activeness_week_var": {
                    "type": "double"
                },
                "activeness_week_sum": {
                    "type": "double"
                },
                "activeness_month_ave": {
                    "type": "double"
                },
                "activeness_month_var": {
                    "type": "double"
                },
                "activeness_month_sum": {
                    "type": "double"
                },
                "activeness_day_change": {
                    "type": "double"
                },
                "activeness_month_change": {
                    "type": "double"
                },
                "activeness_week_change": {
                    "type": "double"
                },
                "politics": {
                    "type": "string",
                    "index": "not_analyzed"
                },
                "domain": {
                    "type": "string",
                    "index": "not_analyzed"
                },
                "hashtag":{
                    "type": "string",
                    "analyzer": "my_analyzer"
                },
                "sensitive_words_string":{
                    "type": "string",
                    "analyzer": "my_analyzer"
                },
                "topic_string":{
                    "type": "string",
                    "analyzer": "my_analyzer"
                },
                "activity_geo":{
                    "type": "string",
                    "analyzer": "my_analyzer"
                }
            }
        }
    }
}


if __name__ == "__main__":
    exist_bool = es.indices.exists(index="copy_user_portrait_activeness")
    print exist_bool
    if not exist_bool:
        es.indices.create(index="copy_user_portrait_activeness", body=index_info, ignore=400)

