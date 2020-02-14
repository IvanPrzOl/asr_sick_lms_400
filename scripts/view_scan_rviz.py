#!/usr/bin/env python   
import rospy
from asr_sick_lms_400.msg import PhenocarLaserScan
from sensor_msgs.msg import LaserScan

class view_scan(object):
    def __init__(self):
        rospy.init_node('view_scan')
        self._scan_sub = rospy.Subscriber('/laserMapping/laser_scan_encoder',LaserScan,self._extractScanLine)
        self._scan_pub = rospy.Publisher('laser_scan',LaserScan,queue_size = 20)

    def _extractScanLine(self,data):
        scanedLine = LaserScan()
        scanedLine.header.stamp = rospy.Time.now()
        scanedLine.header.frame_id = 'lms400_base'
        scanedLine.angle_min = data.angle_min
        scanedLine.angle_max = data.angle_max
        scanedLine.angle_increment = data.angle_increment
        scanedLine.time_increment = data.time_increment
        scanedLine.scan_time = data.scan_time
        scanedLine.range_min = data.range_min
        scanedLine.range_max = data.range_max
        scanedLine.ranges = data.ranges
        scanedLine.intensities = data.intensities
        
        self._scan_pub.publish(scanedLine)


if __name__ == '__main__':
    view_scan_node = view_scan()
    rospy.spin()