secPerMin = 60
secPerHour = 60 * secPerMin
secPerDay = 24 * secPerHour
secs = int(input())

time = []

if secs // secPerDay > 0:
	time.append(str(secs//secPerDay)+':day')
	secs = secs % secPerDay
if secs // secPerHour > 0:
	time.append(str(secs//secPerHour)+':hour')
	secs = secs % secPerHour
if secs // secPerMin > 0:
	time.append(str(secs//secPerMin)+':min')
	secs = secs % secPerMin
if secs > 0:
	time.append(str(secs)+':second')

print(time)
