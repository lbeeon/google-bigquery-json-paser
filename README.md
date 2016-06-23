#Google Big Query json schema paser

##How to use
	
1. Put *.json files in dir "json_file",

2. run "python bigquery_schema_paser.py"

3. Get *.schema files in dir "schema_file"

##Example
Input

	{
	    "kind": "person",
	    "fullName": "John Doe",
	    "age": 22,
	    "gender": "Male",
	    "phoneNumber": {
	        "areaCode": "206",
	        "number": "1234567"
	    },
	    "children": [
	        {
	            "name": "Jane",
	            "gender": "Female",
	            "age": "6"
	        },
	        {
	            "name": "John",
	            "gender": "Male",
	            "age": "15"
	        }
	    ],
	    "citiesLived": [
	        {
	            "place": "Seattle",
	            "yearsLived": [
	                "1995"
	            ]
	        },
	        {
	            "place": "Stockholm",
	            "yearsLived": [
	                "2005"
	            ]
	        }
	    ]
	}

Output

	[
	   {
	      "name":"kind",
	      "mode":"NULLABLE",
	      "type":"STRING"
	   },
	   {
	      "name":"gender",
	      "mode":"NULLABLE",
	      "type":"STRING"
	   },
	   {
	      "name":"age",
	      "mode":"NULLABLE",
	      "type":"INTEGER"
	   },
	   {
	      "name":"citiesLived",
	      "mode":"REPEATED",
	      "type":"RECORD",
	      "fields":[
	         {
	            "name":"yearsLived",
	            "mode":"REPEATED",
	            "type":"RECORD",
	            "fields":[
	
	            ]
	         },
	         {
	            "name":"place",
	            "mode":"NULLABLE",
	            "type":"STRING"
	         }
	      ]
	   },
	   {
	      "name":"phoneNumber",
	      "mode":"NULLABLE",
	      "type":"RECORD",
	      "fields":[
	         {
	            "name":"areaCode",
	            "mode":"NULLABLE",
	            "type":"STRING"
	         },
	         {
	            "name":"number",
	            "mode":"NULLABLE",
	            "type":"STRING"
	         }
	      ]
	   },
	   {
	      "name":"fullName",
	      "mode":"NULLABLE",
	      "type":"STRING"
	   },
	   {
	      "name":"children",
	      "mode":"REPEATED",
	      "type":"RECORD",
	      "fields":[
	         {
	            "name":"gender",
	            "mode":"NULLABLE",
	            "type":"STRING"
	         },
	         {
	            "name":"age",
	            "mode":"NULLABLE",
	            "type":"STRING"
	         },
	         {
	            "name":"name",
	            "mode":"NULLABLE",
	            "type":"STRING"
	         }
	      ]
	   }
	]