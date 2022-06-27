import json
import urllib.request as request

def get_pypi_info_json(module_name):
	resp = request.urlopen( \
					f'https://pypi.org/pypi/{module_name}/json')
	

	jtxt = resp.read()
	d = json.loads(jtxt)
	return d
	
def get_version_url(module_name, version=None):
	dic = get_pypi_info_json(module_name)
	if version is None or version == '':
		version = dic['info']['version']
	url = None
	for r in dic['releases'][version]:
		if r['packagetype'] == 'sdist':
			url = r['url']
			break
	return version, url

