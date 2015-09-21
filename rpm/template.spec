Name:           ros-indigo-ros-comm
Version:        1.11.14
Release:        0%{?dist}
Summary:        ROS ros_comm package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ros_comm
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-message-filters
Requires:       ros-indigo-ros
Requires:       ros-indigo-rosbag
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rosgraph
Requires:       ros-indigo-rosgraph-msgs
Requires:       ros-indigo-roslaunch
Requires:       ros-indigo-roslisp
Requires:       ros-indigo-rosmaster
Requires:       ros-indigo-rosmsg
Requires:       ros-indigo-rosnode
Requires:       ros-indigo-rosout
Requires:       ros-indigo-rosparam
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rosservice
Requires:       ros-indigo-rostest
Requires:       ros-indigo-rostopic
Requires:       ros-indigo-roswtf
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-topic-tools
Requires:       ros-indigo-xmlrpcpp
BuildRequires:  ros-indigo-catkin

%description
ROS communications-related packages, including core client libraries (roscpp,
rospy) and graph introspection tools (rostopic, rosnode, rosservice, rosparam).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Sep 20 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.14-0
- Autogenerated by Bloom

* Tue Apr 28 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.13-0
- Autogenerated by Bloom

* Mon Apr 27 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.12-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.11-0
- Autogenerated by Bloom

* Mon Dec 22 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.10-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.9-0
- Autogenerated by Bloom

* Mon Aug 04 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.8-0
- Autogenerated by Bloom

