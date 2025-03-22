import qrcode

url = "http://192.168.50.136:5000/menu"  # Replace with your local IP

qr = qrcode.make(url)
qr.save("table_scan_qr.png")

print("QR code updated and saved as 'table_scan_qr.png'")
