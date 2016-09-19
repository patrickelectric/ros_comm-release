Name:           ros-kinetic-roslz4
Version:        1.12.4
Release:        0%{?dist}
Summary:        ROS roslz4 package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       lz4-devel
BuildRequires:  lz4-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-rosunit

%description
A Python and C++ implementation of the LZ4 streaming format. Large data streams
are split into blocks which are compressed using the very fast LZ4 compression
algorithm.

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
* Mon Sep 19 2016 Ben Charrow <bcharrow@seas.upenn.edu> - 1.12.4-0
- Autogenerated by Bloom

* Fri Jun 03 2016 Ben Charrow <bcharrow@seas.upenn.edu> - 1.12.2-0
- Autogenerated by Bloom

* Fri Mar 18 2016 Ben Charrow <bcharrow@seas.upenn.edu> - 1.12.0-0
- Autogenerated by Bloom

* Fri Mar 11 2016 Ben Charrow <bcharrow@seas.upenn.edu> - 1.11.17-0
- Autogenerated by Bloom

