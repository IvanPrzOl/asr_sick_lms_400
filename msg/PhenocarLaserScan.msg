Header header            # timestamp in the header is the acquisition time of 
                         
float32 angle_min        # start angle of the scan [rad]
float32 angle_max        # end angle of the scan [rad]
float32 angle_increment  # angular distance between measurements [rad]

float32 time_increment   # time between measurements [seconds] - if your scanner
                         # is moving, this will be used in interpolating position
                         # of 3d points
float32 scan_time        # time between scans [seconds]
uint16 scan_counter      # counter, starting with the first scan after confirmation of the measured value telegram
uint16 telegram_counter  # counter, starting with the first scan after confirmation of the measured value telegram
uint16 system_counter    # Enables the relative time difference between two measured values telegrams to be calculated, information in 1/327.68 us

float32 range_min        # minimum range value [m]
float32 range_max        # maximum range value [m]

float32[] ranges         # range data [m] (Note: values < range_min or > range_max should be discarded)
float32[] intensities    # intensity data [device-specific units].  If your
                         # device does not provide intensities, please leave
                         # the array empty.