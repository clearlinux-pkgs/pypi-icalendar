#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-icalendar
Version  : 4.1.0
Release  : 65
URL      : https://files.pythonhosted.org/packages/32/26/f6d896b78f21a6eb640dac940abb7617f5a910fd7c9b4c213d7b4261f253/icalendar-4.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/32/26/f6d896b78f21a6eb640dac940abb7617f5a910fd7c9b4c213d7b4261f253/icalendar-4.1.0.tar.gz
Summary  : iCalendar parser/generator
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-icalendar-bin = %{version}-%{release}
Requires: pypi-icalendar-license = %{version}-%{release}
Requires: pypi-icalendar-python = %{version}-%{release}
Requires: pypi-icalendar-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(pytz)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
==========================================================
Internet Calendaring and Scheduling (iCalendar) for Python
==========================================================

%package bin
Summary: bin components for the pypi-icalendar package.
Group: Binaries
Requires: pypi-icalendar-license = %{version}-%{release}

%description bin
bin components for the pypi-icalendar package.


%package license
Summary: license components for the pypi-icalendar package.
Group: Default

%description license
license components for the pypi-icalendar package.


%package python
Summary: python components for the pypi-icalendar package.
Group: Default
Requires: pypi-icalendar-python3 = %{version}-%{release}

%description python
python components for the pypi-icalendar package.


%package python3
Summary: python3 components for the pypi-icalendar package.
Group: Default
Requires: python3-core
Provides: pypi(icalendar)
Requires: pypi(python_dateutil)
Requires: pypi(pytz)

%description python3
python3 components for the pypi-icalendar package.


%prep
%setup -q -n icalendar-4.1.0
cd %{_builddir}/icalendar-4.1.0
pushd ..
cp -a icalendar-4.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672280588
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-icalendar
cp %{_builddir}/icalendar-%{version}/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-icalendar/2615805ee0a7d616a284264feb385df7f0791482 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/icalendar

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-icalendar/2615805ee0a7d616a284264feb385df7f0791482

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
