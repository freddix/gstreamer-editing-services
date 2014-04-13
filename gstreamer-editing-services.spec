%include	/usr/lib/rpm/macros.gstreamer

%define		gst_major_ver	1.0
%define		gst_req_ver	1.0
%define		gstpb_req_ver	1.0

Summary:	GStreamer Editing Services
Name:		gstreamer-editing-services
Version:	1.2.0
Release:	0.1
License:	LGPL
Group:		Applications/Multimedia
Source0:	http://gstreamer.freedesktop.org/src/gstreamer-editing-services/%{name}-%{version}.tar.xz
# Source0-md5:	0f77372c7e12395db68b2e1399490b31
URL:		http://gnonlin.sourceforge.net/
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_req_ver}
BuildRequires:	rpm-gstreamerprov
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GES (GStreamer Editing Services) is a cross-platform library that sits
on top of GStreamer and GNonLin. GES simplifies the creation of
multimedia editing applications. Basically, GES is a complete SDK
for making a video editor (but not only that).

%prep
%setup -q

%build
%if 0
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoheader}
%{__automake}
%{__autoconf}
%endif
ulimit -c unlimited
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gst_major_ver}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgnl.so

