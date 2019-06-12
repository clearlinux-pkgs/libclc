#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libclc
Version  : 9f6204ec04a8cadb6bef57caa71e3161c4f398f2
Release  : 2
URL      : https://github.com/llvm-mirror/libclc/archive/9f6204ec04a8cadb6bef57caa71e3161c4f398f2.tar.gz
Source0  : https://github.com/llvm-mirror/libclc/archive/9f6204ec04a8cadb6bef57caa71e3161c4f398f2.tar.gz
Summary  : Library requirements of the OpenCL C programming language
Group    : Development/Tools
License  : Apache-2.0
Requires: libclc-data = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : llvm-dev

%description
libclc
------
libclc is an open source, BSD licensed implementation of the library
requirements of the OpenCL C programming language, as specified by the
OpenCL 1.1 Specification. The following sections of the specification
impose library requirements:

%package data
Summary: data components for the libclc package.
Group: Data

%description data
data components for the libclc package.


%package dev
Summary: dev components for the libclc package.
Group: Development
Requires: libclc-data = %{version}-%{release}
Provides: libclc-devel = %{version}-%{release}
Requires: libclc = %{version}-%{release}

%description dev
dev components for the libclc package.


%prep
%setup -q -n libclc-9f6204ec04a8cadb6bef57caa71e3161c4f398f2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559858104
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -march=haswell "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -march=haswell "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../clr-build-avx2;
make test || :

%install
export SOURCE_DATE_EPOCH=1559858104
rm -rf %{buildroot}
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/clc/amdgcn--amdhsa.bc
/usr/share/clc/aruba-r600--.bc
/usr/share/clc/barts-r600--.bc
/usr/share/clc/bonaire-amdgcn--.bc
/usr/share/clc/bonaire-amdgcn-mesa-mesa3d.bc
/usr/share/clc/caicos-r600--.bc
/usr/share/clc/carrizo-amdgcn--.bc
/usr/share/clc/carrizo-amdgcn-mesa-mesa3d.bc
/usr/share/clc/cayman-r600--.bc
/usr/share/clc/cedar-r600--.bc
/usr/share/clc/cypress-r600--.bc
/usr/share/clc/fiji-amdgcn--.bc
/usr/share/clc/fiji-amdgcn-mesa-mesa3d.bc
/usr/share/clc/gfx900-amdgcn--.bc
/usr/share/clc/gfx900-amdgcn-mesa-mesa3d.bc
/usr/share/clc/gfx902-amdgcn--.bc
/usr/share/clc/gfx902-amdgcn-mesa-mesa3d.bc
/usr/share/clc/gfx904-amdgcn--.bc
/usr/share/clc/gfx904-amdgcn-mesa-mesa3d.bc
/usr/share/clc/gfx906-amdgcn--.bc
/usr/share/clc/gfx906-amdgcn-mesa-mesa3d.bc
/usr/share/clc/hainan-amdgcn--.bc
/usr/share/clc/hainan-amdgcn-mesa-mesa3d.bc
/usr/share/clc/hawaii-amdgcn--.bc
/usr/share/clc/hawaii-amdgcn-mesa-mesa3d.bc
/usr/share/clc/hemlock-r600--.bc
/usr/share/clc/iceland-amdgcn--.bc
/usr/share/clc/iceland-amdgcn-mesa-mesa3d.bc
/usr/share/clc/juniper-r600--.bc
/usr/share/clc/kabini-amdgcn--.bc
/usr/share/clc/kabini-amdgcn-mesa-mesa3d.bc
/usr/share/clc/kaveri-amdgcn--.bc
/usr/share/clc/kaveri-amdgcn-mesa-mesa3d.bc
/usr/share/clc/mullins-amdgcn--.bc
/usr/share/clc/mullins-amdgcn-mesa-mesa3d.bc
/usr/share/clc/nvptx--.bc
/usr/share/clc/nvptx--nvidiacl.bc
/usr/share/clc/nvptx64--.bc
/usr/share/clc/nvptx64--nvidiacl.bc
/usr/share/clc/oland-amdgcn--.bc
/usr/share/clc/oland-amdgcn-mesa-mesa3d.bc
/usr/share/clc/palm-r600--.bc
/usr/share/clc/pitcairn-amdgcn--.bc
/usr/share/clc/pitcairn-amdgcn-mesa-mesa3d.bc
/usr/share/clc/polaris10-amdgcn--.bc
/usr/share/clc/polaris10-amdgcn-mesa-mesa3d.bc
/usr/share/clc/polaris11-amdgcn--.bc
/usr/share/clc/polaris11-amdgcn-mesa-mesa3d.bc
/usr/share/clc/redwood-r600--.bc
/usr/share/clc/stoney-amdgcn--.bc
/usr/share/clc/stoney-amdgcn-mesa-mesa3d.bc
/usr/share/clc/sumo-r600--.bc
/usr/share/clc/sumo2-r600--.bc
/usr/share/clc/tahiti-amdgcn--.bc
/usr/share/clc/tahiti-amdgcn-mesa-mesa3d.bc
/usr/share/clc/tonga-amdgcn--.bc
/usr/share/clc/tonga-amdgcn-mesa-mesa3d.bc
/usr/share/clc/turks-r600--.bc
/usr/share/clc/verde-amdgcn--.bc
/usr/share/clc/verde-amdgcn-mesa-mesa3d.bc

%files dev
%defattr(-,root,root,-)
/usr/include/clc/as_type.h
/usr/include/clc/async/async_work_group_copy.h
/usr/include/clc/async/async_work_group_copy.inc
/usr/include/clc/async/async_work_group_strided_copy.h
/usr/include/clc/async/async_work_group_strided_copy.inc
/usr/include/clc/async/gentype.inc
/usr/include/clc/async/prefetch.h
/usr/include/clc/async/prefetch.inc
/usr/include/clc/async/wait_group_events.h
/usr/include/clc/atom_decl_int32.inc
/usr/include/clc/atom_decl_int64.inc
/usr/include/clc/atomic/atomic_add.h
/usr/include/clc/atomic/atomic_and.h
/usr/include/clc/atomic/atomic_cmpxchg.h
/usr/include/clc/atomic/atomic_dec.h
/usr/include/clc/atomic/atomic_decl.inc
/usr/include/clc/atomic/atomic_inc.h
/usr/include/clc/atomic/atomic_max.h
/usr/include/clc/atomic/atomic_min.h
/usr/include/clc/atomic/atomic_or.h
/usr/include/clc/atomic/atomic_sub.h
/usr/include/clc/atomic/atomic_xchg.h
/usr/include/clc/atomic/atomic_xor.h
/usr/include/clc/cl_khr_global_int32_base_atomics/atom_add.h
/usr/include/clc/cl_khr_global_int32_base_atomics/atom_cmpxchg.h
/usr/include/clc/cl_khr_global_int32_base_atomics/atom_dec.h
/usr/include/clc/cl_khr_global_int32_base_atomics/atom_inc.h
/usr/include/clc/cl_khr_global_int32_base_atomics/atom_sub.h
/usr/include/clc/cl_khr_global_int32_base_atomics/atom_xchg.h
/usr/include/clc/cl_khr_global_int32_extended_atomics/atom_and.h
/usr/include/clc/cl_khr_global_int32_extended_atomics/atom_max.h
/usr/include/clc/cl_khr_global_int32_extended_atomics/atom_min.h
/usr/include/clc/cl_khr_global_int32_extended_atomics/atom_or.h
/usr/include/clc/cl_khr_global_int32_extended_atomics/atom_xor.h
/usr/include/clc/cl_khr_int64_base_atomics/atom_add.h
/usr/include/clc/cl_khr_int64_base_atomics/atom_cmpxchg.h
/usr/include/clc/cl_khr_int64_base_atomics/atom_dec.h
/usr/include/clc/cl_khr_int64_base_atomics/atom_inc.h
/usr/include/clc/cl_khr_int64_base_atomics/atom_sub.h
/usr/include/clc/cl_khr_int64_base_atomics/atom_xchg.h
/usr/include/clc/cl_khr_int64_extended_atomics/atom_and.h
/usr/include/clc/cl_khr_int64_extended_atomics/atom_max.h
/usr/include/clc/cl_khr_int64_extended_atomics/atom_min.h
/usr/include/clc/cl_khr_int64_extended_atomics/atom_or.h
/usr/include/clc/cl_khr_int64_extended_atomics/atom_xor.h
/usr/include/clc/cl_khr_local_int32_base_atomics/atom_add.h
/usr/include/clc/cl_khr_local_int32_base_atomics/atom_cmpxchg.h
/usr/include/clc/cl_khr_local_int32_base_atomics/atom_dec.h
/usr/include/clc/cl_khr_local_int32_base_atomics/atom_inc.h
/usr/include/clc/cl_khr_local_int32_base_atomics/atom_sub.h
/usr/include/clc/cl_khr_local_int32_base_atomics/atom_xchg.h
/usr/include/clc/cl_khr_local_int32_extended_atomics/atom_and.h
/usr/include/clc/cl_khr_local_int32_extended_atomics/atom_max.h
/usr/include/clc/cl_khr_local_int32_extended_atomics/atom_min.h
/usr/include/clc/cl_khr_local_int32_extended_atomics/atom_or.h
/usr/include/clc/cl_khr_local_int32_extended_atomics/atom_xor.h
/usr/include/clc/clc.h
/usr/include/clc/clcfunc.h
/usr/include/clc/clcmacros.h
/usr/include/clc/clctypes.h
/usr/include/clc/common/degrees.h
/usr/include/clc/common/degrees.inc
/usr/include/clc/common/mix.h
/usr/include/clc/common/mix.inc
/usr/include/clc/common/radians.h
/usr/include/clc/common/radians.inc
/usr/include/clc/common/sign.h
/usr/include/clc/common/smoothstep.h
/usr/include/clc/common/smoothstep.inc
/usr/include/clc/common/step.h
/usr/include/clc/common/step.inc
/usr/include/clc/convert.h
/usr/include/clc/explicit_fence/explicit_memory_fence.h
/usr/include/clc/float/definitions.h
/usr/include/clc/geometric/cross.h
/usr/include/clc/geometric/distance.h
/usr/include/clc/geometric/distance.inc
/usr/include/clc/geometric/dot.h
/usr/include/clc/geometric/dot.inc
/usr/include/clc/geometric/fast_distance.h
/usr/include/clc/geometric/fast_distance.inc
/usr/include/clc/geometric/fast_length.h
/usr/include/clc/geometric/fast_length.inc
/usr/include/clc/geometric/fast_normalize.h
/usr/include/clc/geometric/fast_normalize.inc
/usr/include/clc/geometric/floatn.inc
/usr/include/clc/geometric/length.h
/usr/include/clc/geometric/length.inc
/usr/include/clc/geometric/normalize.h
/usr/include/clc/geometric/normalize.inc
/usr/include/clc/image/image.h
/usr/include/clc/image/image_defines.h
/usr/include/clc/integer/abs.h
/usr/include/clc/integer/abs.inc
/usr/include/clc/integer/abs_diff.h
/usr/include/clc/integer/abs_diff.inc
/usr/include/clc/integer/add_sat.h
/usr/include/clc/integer/add_sat.inc
/usr/include/clc/integer/clz.h
/usr/include/clc/integer/clz.inc
/usr/include/clc/integer/definitions.h
/usr/include/clc/integer/gentype.inc
/usr/include/clc/integer/hadd.h
/usr/include/clc/integer/hadd.inc
/usr/include/clc/integer/integer-gentype.inc
/usr/include/clc/integer/mad24.h
/usr/include/clc/integer/mad24.inc
/usr/include/clc/integer/mad_hi.h
/usr/include/clc/integer/mad_sat.h
/usr/include/clc/integer/mad_sat.inc
/usr/include/clc/integer/mul24.h
/usr/include/clc/integer/mul24.inc
/usr/include/clc/integer/mul_hi.h
/usr/include/clc/integer/mul_hi.inc
/usr/include/clc/integer/popcount.h
/usr/include/clc/integer/rhadd.h
/usr/include/clc/integer/rhadd.inc
/usr/include/clc/integer/rotate.h
/usr/include/clc/integer/rotate.inc
/usr/include/clc/integer/sub_sat.h
/usr/include/clc/integer/sub_sat.inc
/usr/include/clc/integer/unary.inc
/usr/include/clc/integer/upsample.h
/usr/include/clc/math/acos.h
/usr/include/clc/math/acosh.h
/usr/include/clc/math/acospi.h
/usr/include/clc/math/asin.h
/usr/include/clc/math/asinh.h
/usr/include/clc/math/asinpi.h
/usr/include/clc/math/atan.h
/usr/include/clc/math/atan2.h
/usr/include/clc/math/atan2pi.h
/usr/include/clc/math/atanh.h
/usr/include/clc/math/atanpi.h
/usr/include/clc/math/binary_decl.inc
/usr/include/clc/math/binary_decl_tt.inc
/usr/include/clc/math/cbrt.h
/usr/include/clc/math/ceil.h
/usr/include/clc/math/copysign.h
/usr/include/clc/math/cos.h
/usr/include/clc/math/cosh.h
/usr/include/clc/math/cospi.h
/usr/include/clc/math/erf.h
/usr/include/clc/math/erfc.h
/usr/include/clc/math/exp.h
/usr/include/clc/math/exp10.h
/usr/include/clc/math/exp2.h
/usr/include/clc/math/expm1.h
/usr/include/clc/math/fabs.h
/usr/include/clc/math/fdim.h
/usr/include/clc/math/floor.h
/usr/include/clc/math/fma.h
/usr/include/clc/math/fmax.h
/usr/include/clc/math/fmin.h
/usr/include/clc/math/fmod.h
/usr/include/clc/math/fract.h
/usr/include/clc/math/fract.inc
/usr/include/clc/math/frexp.h
/usr/include/clc/math/frexp.inc
/usr/include/clc/math/gentype.inc
/usr/include/clc/math/half_cos.h
/usr/include/clc/math/half_divide.h
/usr/include/clc/math/half_exp.h
/usr/include/clc/math/half_exp10.h
/usr/include/clc/math/half_exp2.h
/usr/include/clc/math/half_log.h
/usr/include/clc/math/half_log10.h
/usr/include/clc/math/half_log2.h
/usr/include/clc/math/half_powr.h
/usr/include/clc/math/half_recip.h
/usr/include/clc/math/half_rsqrt.h
/usr/include/clc/math/half_sin.h
/usr/include/clc/math/half_sqrt.h
/usr/include/clc/math/half_tan.h
/usr/include/clc/math/hypot.h
/usr/include/clc/math/ilogb.h
/usr/include/clc/math/ilogb.inc
/usr/include/clc/math/ldexp.h
/usr/include/clc/math/ldexp.inc
/usr/include/clc/math/lgamma.h
/usr/include/clc/math/lgamma_r.h
/usr/include/clc/math/lgamma_r.inc
/usr/include/clc/math/log.h
/usr/include/clc/math/log10.h
/usr/include/clc/math/log1p.h
/usr/include/clc/math/log2.h
/usr/include/clc/math/logb.h
/usr/include/clc/math/mad.h
/usr/include/clc/math/maxmag.h
/usr/include/clc/math/minmag.h
/usr/include/clc/math/modf.h
/usr/include/clc/math/modf.inc
/usr/include/clc/math/nan.h
/usr/include/clc/math/nan.inc
/usr/include/clc/math/native_cos.h
/usr/include/clc/math/native_divide.h
/usr/include/clc/math/native_exp.h
/usr/include/clc/math/native_exp10.h
/usr/include/clc/math/native_exp2.h
/usr/include/clc/math/native_log.h
/usr/include/clc/math/native_log10.h
/usr/include/clc/math/native_log2.h
/usr/include/clc/math/native_powr.h
/usr/include/clc/math/native_recip.h
/usr/include/clc/math/native_rsqrt.h
/usr/include/clc/math/native_sin.h
/usr/include/clc/math/native_sqrt.h
/usr/include/clc/math/native_tan.h
/usr/include/clc/math/nextafter.h
/usr/include/clc/math/pow.h
/usr/include/clc/math/pown.h
/usr/include/clc/math/pown.inc
/usr/include/clc/math/powr.h
/usr/include/clc/math/remainder.h
/usr/include/clc/math/remquo.h
/usr/include/clc/math/remquo.inc
/usr/include/clc/math/rint.h
/usr/include/clc/math/rootn.h
/usr/include/clc/math/rootn.inc
/usr/include/clc/math/round.h
/usr/include/clc/math/rsqrt.h
/usr/include/clc/math/sin.h
/usr/include/clc/math/sincos.h
/usr/include/clc/math/sincos.inc
/usr/include/clc/math/sinh.h
/usr/include/clc/math/sinpi.h
/usr/include/clc/math/sqrt.h
/usr/include/clc/math/tan.h
/usr/include/clc/math/tanh.h
/usr/include/clc/math/tanpi.h
/usr/include/clc/math/ternary_decl.inc
/usr/include/clc/math/tgamma.h
/usr/include/clc/math/trunc.h
/usr/include/clc/math/unary_decl.inc
/usr/include/clc/misc/shuffle.h
/usr/include/clc/misc/shuffle2.h
/usr/include/clc/relational/all.h
/usr/include/clc/relational/any.h
/usr/include/clc/relational/binary_decl.inc
/usr/include/clc/relational/bitselect.h
/usr/include/clc/relational/bitselect.inc
/usr/include/clc/relational/floatn.inc
/usr/include/clc/relational/isequal.h
/usr/include/clc/relational/isfinite.h
/usr/include/clc/relational/isgreater.h
/usr/include/clc/relational/isgreaterequal.h
/usr/include/clc/relational/isinf.h
/usr/include/clc/relational/isless.h
/usr/include/clc/relational/islessequal.h
/usr/include/clc/relational/islessgreater.h
/usr/include/clc/relational/isnan.h
/usr/include/clc/relational/isnormal.h
/usr/include/clc/relational/isnotequal.h
/usr/include/clc/relational/isordered.h
/usr/include/clc/relational/isunordered.h
/usr/include/clc/relational/select.h
/usr/include/clc/relational/select.inc
/usr/include/clc/relational/signbit.h
/usr/include/clc/relational/unary_decl.inc
/usr/include/clc/shared/clamp.h
/usr/include/clc/shared/clamp.inc
/usr/include/clc/shared/max.h
/usr/include/clc/shared/max.inc
/usr/include/clc/shared/min.h
/usr/include/clc/shared/min.inc
/usr/include/clc/shared/vload.h
/usr/include/clc/shared/vstore.h
/usr/include/clc/synchronization/barrier.h
/usr/include/clc/synchronization/cl_mem_fence_flags.h
/usr/include/clc/workitem/get_global_id.h
/usr/include/clc/workitem/get_global_offset.h
/usr/include/clc/workitem/get_global_size.h
/usr/include/clc/workitem/get_group_id.h
/usr/include/clc/workitem/get_local_id.h
/usr/include/clc/workitem/get_local_size.h
/usr/include/clc/workitem/get_num_groups.h
/usr/include/clc/workitem/get_work_dim.h
/usr/lib64/pkgconfig/libclc.pc
