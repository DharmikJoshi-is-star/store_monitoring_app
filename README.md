# store_monitoring_app


<h3>Trigger Report generation<h3> 
<br>
Method: POST
URL: http://localhost:5000/api/v1/trigger_report
CURL: curl --location --request POST 'http://localhost:5000/api/v1/trigger_report?no_stores=10'

Sample Request:-
curl --location --request POST 'http://localhost:5000/api/v1/trigger_report?no_stores=10'

Response:-
{
    "report_id": "95e7af35-578c-42ef-8c0a-ae1744a3eb0a"
}

API Spec:-
Request Params=>  no_stores: to generate report for first n stores this params can be send

Response=> 
report_id: "refernce unique id to retreive the status of report"

<hr>

<h3>Get Report status</h3>

<br>

Method: GET
URL: http://localhost:5000/api/v1/get_report/95e7af35-578c-42ef-8c0a-ae1744a3eb0a
CURL: curl --location 'http://localhost:5000/api/v1/get_report/95e7af35-578c-42ef-8c0a-ae1744a3eb0a'

Sample Request:-
curl --location 'http://localhost:5000/api/v1/get_report/95e7af35-578c-42ef-8c0a-ae1744a3eb0a'

Response:-
{
    "report_file_in_base64": "c3RvcmVfaWQsdXB0aW1lX2xhc3RfaG91cix1cHRpbWVfbGFzdF9kYXksdXBkYXRlX2xhc3Rfd2Vlayxkb3dudGltZV9sYXN0X2hvdXIsZG93bnRpbWVfbGFzdF9kYXksZG93bnRpbWVfbGFzdF93ZWVrDQoxMDAwMzg1NDEyMDQxNDA4NTY1LDAsMC45NDEzODg4ODg4ODg4ODg5LDEwNi4zMDkxNjY2NjY2NjY2NywwLDE2Ljk5Njk0NDQ0NDQ0NDQ0NSw1NS42NjA4MzMzMzMzMzMzMzYNCjEwMDA1NTg0NDE1MzU1MjA1NjYsMCwwLjAsNjQuMDM5NDQ0NDQ0NDQ0NDQsMCw2LjkxMzg4ODg4ODg4ODg4OSw4Ni45NTkxNjY2NjY2NjY2Mg0KMTAwMzIwMDYxNDc3MDI0NDc5OSwwLDE4LjEwMjc3Nzc3Nzc3Nzc3OCwxNjEuOTgzNjExMTExMTExMTQsMCwwLjAsMC4wDQoxMDA1NDU0NDA4NzQ3MzA1Njc5LDAsNy4wMzYzODg4ODg4ODg4ODksMTQ5LjAyNTU1NTU1NTU1NTU3LDAsMC4wLDEuOTk2NjY2NjY2NjY2NjY2OA0KMTAwNzM5MjI3ODQ1OTU3MzEwMCwwLDYuOTk2OTQ0NDQ0NDQ0NDQ0LDE1MS40OTcyMjIyMjIyMjIyLDAsMC4wLDAuMA0K",
    "report_status": "Complete",
    "report_file": "/tmp/95e7af35-578c-42ef-8c0a-ae1744a3eb0a.csv"
}

Request:=> 
report-id(Request param): unique id to be passed to get report status 

Response=> 
report_file_in_base64: csv generated report file in base64 format
report_status: Running/Complete
report_file: Generate report file path on local system can also used to upload on thrird party like s3 bucket


======Testing observations======

for top 10 stores report is getting generate in 10 seconds
and total unqiue store ids present in the store_business_time csv file is "11116"
So to generate report for all stores can take upto 4/5 hours of time.