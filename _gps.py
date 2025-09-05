emergency_number="NOMOR DARURAT KALIAN, USAHAKAN PAKE 628 BUKAN 08, KHUSUS AXIS UNTUK TRIGGER SEND SMS LEWAT OTP LOGIN AXISNET, BISA DI BIARKAN/KOSONGKAN JIKA TIDAK INGIN PAKAI"

import json,time,subprocess,os,base64
from datetime import datetime as dt
log_file="/sdcard/gps_log.json";MAX_LOGS=20;Entry=0
open(log_file,'w').close()
load_logs=lambda:[] if not os.path.exists(log_file) else [json.loads(l) for l in open(log_file).readlines() if l.strip()]
save_logs=lambda l:[open(log_file,'w').write("".join(json.dumps(e)+"\n" for e in l))]
exec(base64.b64decode(b'b3Muc3lzdGVtKCJjbGVhciIp').decode())
exec(base64.b64decode(b'cHJpbnQoIkNyZWF0ZWQgYnkgUmFuZFNmayIp').decode())
def log_gps():
    global Entry; Entry += 1
    data = {}
    r = subprocess.run(['termux-location','-p','gps'], capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        try: data = json.loads(r.stdout)
        except: data = {}
    if not data:
        r = subprocess.run(['termux-location','-p','network'], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            try: data = json.loads(r.stdout)
            except: data = {}
    l = load_logs(); l.pop(0) if len(l) >= MAX_LOGS else None
    l.append({'entry': Entry, 'timestamp': str(dt.now()), **data})
    save_logs(l)
    print("Location logged (Entry #{})".format(Entry))
check_sms_trigger=lambda pw="KATA SANDI KAMU":(lambda sms: (lambda b,s: ("SENDLOG" in b and subprocess.run(['termux-sms-send','-n',s,json.dumps(load_logs())]) and print("Sent logs to {}".format(s))) or ("AXIS" in s and pw.upper() in b and subprocess.run(['termux-sms-send','-n',emergency_number,json.dumps(load_logs())]) and print("Sent logs to emergency number")))(sms[0].get("body","").strip().upper() if sms else "",sms[0].get("address","").upper() if sms else ""))(json.loads(subprocess.run(['termux-sms-list','-l','1'],capture_output=True,text=True).stdout))
while True: 
    (lambda: (log_gps(), check_sms_trigger()))() if not (lambda e=None: (print(f"Error: {e}"), True) if False else False)() else None; time.sleep(10)