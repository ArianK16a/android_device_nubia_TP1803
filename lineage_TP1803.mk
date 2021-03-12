#
# Copyright (C) 2021 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from TP1803 device
$(call inherit-product, device/nubia/TP1803/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_BRAND := Nubia
PRODUCT_DEVICE := TP1803
PRODUCT_MANUFACTURER := Nubia
PRODUCT_MODEL := Mini 5G
PRODUCT_NAME := lineage_TP1803

PRODUCT_GMS_CLIENTID_BASE := android-nubia
