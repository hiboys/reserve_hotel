import sys
from datetime import datetime
from datetime import date
reload(sys)
sys.setdefaultencoding('utf-8')
def str2date(year, month, day):
	year= int(year)
	month= int(month)
	day= int(day)
	return date(year, month, day)

#set the check_in and check_out to cookie
def set_cookie4date(request, response):
	check_in = str2date(
			request.GET['check_in_year'],
			request.GET['check_in_month'],
			request.GET['check_in_day'],
			)
	check_out = str2date(
			request.GET['check_out_year'],
			request.GET['check_out_month'],
			request.GET['check_out_day'],
			)
	response.set_cookie('check_in', check_in)
	response.set_cookie('check_out',check_out)
	return None

#get the check_in and check_out from cookie
def get_date_from_cookie(request):
	check_in = request.COOKIES.get('check_in')
	check_in = datetime.strptime(check_in, "%Y-%m-%d").date()
	check_out = request.COOKIES.get('check_out')
	check_out= datetime.strptime(check_out, "%Y-%m-%d").date()
	return check_in, check_out

#write the booking data to cookie
def set_cookie4book(response, data):
	response.set_cookie("hotel_id", data["hotel"].id)
	response.set_cookie("room_type", data["room_type"])
	response.set_cookie("room_num", data["room_num"])
	response.set_cookie("check_in", data["check_in"])
	response.set_cookie("check_out", data["check_out"])

def init_select_form(form, check_in, check_out):
	form.fields["check_in"].initial = check_in
	form.fields["check_out"].initial = check_out
