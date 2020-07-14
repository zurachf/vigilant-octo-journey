import usaepay
from usaepay import run_call


def delete(data={}):
	"""Calls /customers/bulk
	Deletes a list of customers.

	Args:
		data (dict) contents:
			Keys (list) required

	Returns:
		Dictionary Status
	"""
	params={}
	path='/customers/bulk'
	data_list = data['Keys']
	return run_call('delete',path,data,params)
