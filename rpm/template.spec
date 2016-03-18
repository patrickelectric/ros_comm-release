Name:           ros-kinetic-ros-comm
Version:        1.12.0
Release:        0%{?dist}
Summary:        ROS ros_comm package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ros_comm
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-message-filters
Requires:       ros-kinetic-ros
Requires:       ros-kinetic-rosbag
Requires:       ros-kinetic-rosconsole
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rosgraph
Requires:       ros-kinetic-rosgraph-msgs
Requires:       ros-kinetic-roslaunch
Requires:       ros-kinetic-roslisp
Requires:       ros-kinetic-rosmaster
Requires:       ros-kinetic-rosmsg
Requires:       ros-kinetic-rosnode
Requires:       ros-kinetic-rosout
Requires:       ros-kinetic-rosparam
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rosservice
Requires:       ros-kinetic-rostest
Requires:       ros-kinetic-rostopic
Requires:       ros-kinetic-roswtf
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-topic-tools
Requires:       ros-kinetic-xmlrpcpp
BuildRequires:  ros-kinetic-catkin

%description
ROS communications-related packages, including core client libraries (roscpp,
rospy) and graph introspection tools (rostopic, rosnode, rosservice, rosparam).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Mar 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.0-0
- Autogenerated by Bloom

* Fri Mar 11 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.17-0
- Autogenerated by Bloom

