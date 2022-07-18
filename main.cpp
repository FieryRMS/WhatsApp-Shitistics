///PROBLEM E
#include<bits/stdc++.h>
using namespace std;
#define endl '\n'

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

map<wchar_t,int> emoji_cnt;
map<wstring, int> Word_cnt;
map<wstring, int> Person_cnt;
map<wstring, int> Replier_cnt;
map<wstring, int> Replied_cnt;
map<wstring, wstring> phone2name;
map<wstring, map<wstring, int> Date_cnt;

bool is_emoji(wchar_t a)
{
    if(a<=127 || a==8204)
        return false;
    return true;
}
int main()
{
	fast;
	freopen("in.txt","r",stdin);
	wstring Message;
	while(getline(wcin,Message))
    {
        if(Message==L"")
            continue;
        wstring Line;
        getline(wcin,Line);
        wstring From;
        getline(wcin,From);
        From.erase(0,5);

        wstring Msg,FullMsg,RepliedTo,Time;
        bool flag=0,RepFlag=0;
        while(getline(wcin,Msg))
        {
            if(Msg.substr(0,9)==L"Message: ") flag=1;
            if(Msg.substr(0,13)==L"Replying to: ")
            {
                RepliedTo=Msg;
                RepliedTo.erase(0,13);
                RepliedTo.erase(RepliedTo.find(L" ")+1);
                RepFlag=1;
            }
            if(Msg.substr(0,11)==L"Timestamp: ")
            {
                break;
            }
            if(flag)
                FullMsg+=Msg+L"\n";
        }

        if(Msg.find(L"System message")==wstring::npos)
        {
            if(From[0]==L'M')From=L"Me";
            else
            {
                From.erase(0,From.find(L"participant ")+12);
                From.erase(From.find(L" "));
            }
            Time=Msg;
            Time.erase(0,11);
            Time.erase(Time.find(L" "));
            //From, FullMsg, RepFlag, RepliedTo, Time
        }
    }
}
