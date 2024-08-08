from speedtest import Speedtest  # استيراد المكتبة لقياس سرعة الإنترنت

wifi = Speedtest()  # إنشاء كائن Speedtest

print("getting download speed...")  # طباعة رسالة للمستخدم
download = wifi.download()  # قياس سرعة التحميل
print(f"Download: {download / 1024 / 1024:.2f} mbps")  # عرض سرعة التحميل بالميجابايت

print("getting upload speed...")  # طباعة رسالة للمستخدم
upload = wifi.upload()  # قياس سرعة الرفع
print(f"Upload: {upload / 1024 / 1024:.2f} mbps")  # عرض سرعة الرفع بالميجابايت
