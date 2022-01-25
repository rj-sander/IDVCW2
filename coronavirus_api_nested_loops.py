from requests import get
import json
import csv

csvFile = open('coronavirus_data.csv', 'w')
csvWriter = csv.writer(csvFile,delimiter =',')
csvWriter.writerow(['area', 'code', 'date', 'newCases'])

boroughs = ["E09000002", "E09000003", "E09000004", "E09000005", "E09000006", "E09000007", "E09000008", "E09000009", "E09000010", "E09000011", "E09000012", "E09000013", "E09000014", "E09000015", "E09000016", "E09000017", "E09000018", "E09000019", "E09000020", "E09000021", "E09000022", "E09000023", "E09000024", "E09000025", "E09000026", "E09000027", "E09000028", "E09000029", "E09000030", "E09000031", "E09000032", "E09000033"]

def get_data(code, currentDay):
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=ltla;areaCode={0};date=2021-12-{1}&'
        'structure={{"date":"date","newCases":"newCasesByPublishDate","area":"areaName","code": "areaCode"}}'
    )

    response = get(endpoint.format(code, currentDay), timeout=10)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')

    return response.json()


for borough in boroughs:
    day = 15
    while day < 25:
        full_text = get_data(borough, day)
        # print(json.dumps(full_text))
        area = full_text['data'][0]["area"]
        code = full_text['data'][0]["code"]
        date = full_text['data'][0]['date']
        newCases = full_text['data'][0]['newCases']
        res = [area, code, date, newCases]
        print(res)

                    # Append the result to the CSV file
        csvWriter.writerow(res)
        day += 1
