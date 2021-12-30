#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-carData
Version  : 3.0.4
Release  : 42
URL      : https://cran.r-project.org/src/contrib/carData_3.0-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/carData_3.0-4.tar.gz
Summary  : Companion to Applied Regression Data Sets
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
Datasets to Accompany J. Fox and S. Weisberg, 
  An R Companion to Applied Regression, Third Edition, Sage (2019).

%prep
%setup -q -c -n carData
cd %{_builddir}/carData

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640905545

%install
export SOURCE_DATE_EPOCH=1640905545
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library carData
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library carData
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library carData
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc carData || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/carData/DESCRIPTION
/usr/lib64/R/library/carData/INDEX
/usr/lib64/R/library/carData/Meta/Rd.rds
/usr/lib64/R/library/carData/Meta/data.rds
/usr/lib64/R/library/carData/Meta/features.rds
/usr/lib64/R/library/carData/Meta/hsearch.rds
/usr/lib64/R/library/carData/Meta/links.rds
/usr/lib64/R/library/carData/Meta/nsInfo.rds
/usr/lib64/R/library/carData/Meta/package.rds
/usr/lib64/R/library/carData/NAMESPACE
/usr/lib64/R/library/carData/NEWS
/usr/lib64/R/library/carData/data/Rdata.rdb
/usr/lib64/R/library/carData/data/Rdata.rds
/usr/lib64/R/library/carData/data/Rdata.rdx
/usr/lib64/R/library/carData/data/datalist
/usr/lib64/R/library/carData/help/AnIndex
/usr/lib64/R/library/carData/help/aliases.rds
/usr/lib64/R/library/carData/help/carData.rdb
/usr/lib64/R/library/carData/help/carData.rdx
/usr/lib64/R/library/carData/help/paths.rds
/usr/lib64/R/library/carData/html/00Index.html
/usr/lib64/R/library/carData/html/R.css
