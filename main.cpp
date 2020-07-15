
#include <urlmon.h>

#pragma comment(lib, "urlmon.lib")
int main()
{
	HRESULT hr = URLDownloadToFile ( NULL, "http://www.cplusplus.com/forum/beginner/109232/", "/var/lib/jenkins/workspace/Hello_C++/report.txt", 0, NULL );
	return 0;
}