Name:           ros-indigo-topic-tools
Version:        1.11.15
Release:        0%{?dist}
Summary:        ROS topic_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/topic_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rostime
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-xmlrpcpp
BuildRequires:  ros-indigo-catkin >= 0.5.78
BuildRequires:  ros-indigo-cpp-common
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-rostime
BuildRequires:  ros-indigo-rosunit
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-xmlrpcpp

%description
Tools for directing, throttling, selecting, and otherwise messing with ROS
topics at a meta level. None of the programs in this package actually know about
the topics whose streams they are altering; instead, these tools deal with
messages as generic binary blobs. This means they can be applied to any ROS
topic.

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
* Tue Oct 13 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.15-0
- Autogenerated by Bloom

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

