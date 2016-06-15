#Google Big Query json schema paser

##How to use
	
1. Put *.json files in dir "json_file",

2. run "python bigquery_schema_paser.py"

3. Get *.schema files in dir "schema_file"

##Example
Input

	{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

Output

	[  
	   {  
	      "name":"glossary",
	      "mode":"NULLABLE",
	      "type":"RECORD",
	      "fields":[  
	         {  
	            "name":"GlossDiv",
	            "mode":"NULLABLE",
	            "type":"RECORD",
	            "fields":[  
	               {  
	                  "name":"GlossList",
	                  "mode":"NULLABLE",
	                  "type":"RECORD",
	                  "fields":[  
	                     {  
	                        "name":"GlossEntry",
	                        "mode":"NULLABLE",
	                        "type":"RECORD",
	                        "fields":[  
	                           {  
	                              "name":"GlossDef",
	                              "mode":"NULLABLE",
	                              "type":"RECORD",
	                              "fields":[  
	                                 {  
	                                    "name":"GlossSeeAlso",
	                                    "mode":"REPEATED",
	                                    "type":"RECORD",
	                                    "fields":[  
	
	                                    ]
	                                 },
	                                 {  
	                                    "name":"para",
	                                    "mode":"NULLABLE",
	                                    "type":"STRING"
	                                 }
	                              ]
	                           },
	                           {  
	                              "name":"GlossSee",
	                              "mode":"NULLABLE",
	                              "type":"STRING"
	                           },
	                           {  
	                              "name":"Acronym",
	                              "mode":"NULLABLE",
	                              "type":"STRING"
	                           },
	                           {  
	                              "name":"GlossTerm",
	                              "mode":"NULLABLE",
	                              "type":"STRING"
	                           },
	                           {  
	                              "name":"Abbrev",
	                              "mode":"NULLABLE",
	                              "type":"STRING"
	                           },
	                           {  
	                              "name":"SortAs",
	                              "mode":"NULLABLE",
	                              "type":"STRING"
	                           },
	                           {  
	                              "name":"ID",
	                              "mode":"NULLABLE",
	                              "type":"STRING"
	                           }
	                        ]
	                     }
	                  ]
	               },
	               {  
	                  "name":"title",
	                  "mode":"NULLABLE",
	                  "type":"STRING"
	               }
	            ]
	         },
	         {  
	            "name":"title",
	            "mode":"NULLABLE",
	            "type":"STRING"
	         }
	      ]
	   }
	]