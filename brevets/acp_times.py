"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at
https://rusa.org/octime_alg.html
https://rusa.org/pages/rulesForRiders
"""
import arrow



#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    brevet_open_time = 0

    brevet_dist_times = {'200': 353, '400': 728, '600': 1128, '1000': 1985}

    if control_dist_km < 200:
        brevet_open_time = (control_dist_km/34*60)

    if 200 <= control_dist_km < 400:
        brevet_open_time = ((control_dist_km%200)/32*60)+brevet_dist_times.get('200')

    if 400 <= control_dist_km < 600:
        brevet_open_time = ((control_dist_km%400)/30*60)+brevet_dist_times.get('400')

    if 600 <= control_dist_km < 1000:
        brevet_open_time = ((control_dist_km%600)/28*60)+brevet_dist_times.get('600')

    if control_dist_km == 1000:
        brevet_open_time = brevet_dist_times.get('1000')

    return brevet_start_time.shift(minutes=brevet_open_time)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    brevet_close_time = 60

    brevet_dist_times = {'200': 800, '400': 1600, '600': 2400, '1000': 4500}

    if 0 < control_dist_km < 200:
        brevet_close_time = control_dist_km/15*60

    if 200 <= control_dist_km < 400:
        brevet_close_time = ((control_dist_km%200)/15*60)+brevet_dist_times.get('200')

    if 400 <= control_dist_km < 600:
        brevet_close_time = ((control_dist_km%400)/15*60)+brevet_dist_times.get('400')

    if 600 <= control_dist_km < 1000:
        brevet_close_time = ((control_dist_km%600)/11.428*60)+brevet_dist_times.get('600')

    if control_dist_km == 1000:
        brevet_close_time = brevet_dist_times.get('1000')

    return brevet_start_time.shift(minutes=brevet_close_time)


