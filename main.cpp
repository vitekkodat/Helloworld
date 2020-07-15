#include <tchar.h>
#include <urlmon.h>

#pragma comment(lib, "urlmon.lib")
int main()
{
	HRESULT hr = URLDownloadToFile ( NULL, _T("http://www.cplusplus.com/forum/beginner/109232/"), _T("/var/lib/jenkins/workspace/Hello_C++/report.txt"), 0, NULL );
	return 0;
}