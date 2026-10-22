$env:TT_SESSIONID = Read-Host "paste your sessionid cookie"
python main.py --targets config/targets.sample.txt --message config/messages/default.txt
</Parameter>