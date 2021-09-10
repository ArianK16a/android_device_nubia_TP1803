#
# Copyright (C) 2020-2021 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

import common
import re

def FullOTA_InstallEnd(info):
    OTA_InstallEnd(info)
    return

def IncrementalOTA_InstallEnd(info):
    OTA_InstallEnd(info)
    return

def AddImage(info, basename, dest):
    name = basename
    data = info.input_zip.read("IMAGES/" + basename)
    common.ZipWriteStr(info.output_zip, name, data)
    info.script.Print("Patching {} image unconditionally...".format(dest.split('/')[-1]))
    info.script.AppendExtra('package_extract_file("%s", "%s");' % (name, dest))

def AddImageRadio(info, basename, dest):
    name = basename
    data = info.input_zip.read("RADIO/" + basename)
    common.ZipWriteStr(info.output_zip, name, data)
    info.script.Print("Patching {} image unconditionally...".format(dest.split('/')[-1]))
    info.script.AppendExtra('package_extract_file("%s", "%s");' % (name, dest))

def OTA_InstallEnd(info):
    AddImage(info, "dtbo.img", "/dev/block/bootdevice/by-name/dtbo")
    AddImage(info, "vbmeta.img", "/dev/block/bootdevice/by-name/vbmeta")

    AddImageRadio(info, "abl.elf", "/dev/block/bootdevice/by-name/abl")
    AddImageRadio(info, "aop.mbn", "/dev/block/bootdevice/by-name/aop")
    AddImageRadio(info, "BTFM.bin", "/dev/block/bootdevice/by-name/bluetooth")
    AddImageRadio(info, "cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib")
    AddImageRadio(info, "cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64")
    AddImageRadio(info, "devcfg.mbn", "/dev/block/bootdevice/by-name/devcfg")
    AddImageRadio(info, "dspso.bin", "/dev/block/bootdevice/by-name/dsp")
    AddImageRadio(info, "hyp.mbn", "/dev/block/bootdevice/by-name/hyp")
    AddImageRadio(info, "imagefv.elf", "/dev/block/bootdevice/by-name/ImageFv")
    AddImageRadio(info, "km4.mbn", "/dev/block/bootdevice/by-name/keymaster")
    AddImageRadio(info, "multi_image.mbn", "/dev/block/bootdevice/by-name/multiimgoem")
    AddImageRadio(info, "NON-HLOS.bin", "/dev/block/bootdevice/by-name/modem")
    AddImageRadio(info, "parameter.img", "/dev/block/bootdevice/by-name/parameter")
    AddImageRadio(info, "qupv3fw.elf", "/dev/block/bootdevice/by-name/qupfw")
    AddImageRadio(info, "splash.bin", "/dev/block/bootdevice/by-name/splash")
    AddImageRadio(info, "storsec.mbn", "/dev/block/bootdevice/by-name/storsec")
    AddImageRadio(info, "tz.mbn", "/dev/block/bootdevice/by-name/tz")
    AddImageRadio(info, "uefi_sec.mbn", "/dev/block/bootdevice/by-name/uefisecapp")
    AddImageRadio(info, "xbl.bin", "/dev/block/bootdevice/by-name/xbl")
    AddImageRadio(info, "xbl_config.bin", "/dev/block/bootdevice/by-name/xbl_config")

    return
