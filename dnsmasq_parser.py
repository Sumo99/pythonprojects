#!/usr/bin/python3
from datetime import datetime
file = open("/var/lib/misc/dnsmasq.leases", "r")
out_file = open("out_test.html")
out_file.write("""<style>
h1{
    top:40px;
    text-align:center;
}
table {
  top:30px;
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}
tr:hover{
    font-size:110%;
}
td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
""")
out_file.write("<h1> Devices currently connected to TechSWiz </h1>")
out_file.write("<table>")
out_file.write("<tr>")
out_file.write("<th> Lease expiry date </th>")
out_file.write("<th> Mac address of the client </th>")
out_file.write("<th> IP address of the client </th>")
out_file.write("<th> Client Hostname </th>")
out_file.write("<th> Mac address that is visible to network </th>")
out_file.write("</tr>")
for line in file:
    out_file.write("<tr>")
    tokenized = line.rstrip('\n').split(" ")
    timestamp = tokenized[0]
    tokenized[0] = datetime.utcfromtimestamp(
        int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    out_file.write("<td>"+tokenized[0]+"</td>")
    out_file.write("<td>"+tokenized[1]+"</td>")
    out_file.write("<td>"+tokenized[2]+"</td>")
    out_file.write("<td>"+tokenized[3]+"</td>")
    out_file.write("<td>"+tokenized[4]+"</td>")
    out_file.write("</tr>")
out_file.write("</table>")
