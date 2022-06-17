#
# Copyright (C) 2022 Teracube-Inc
#

EMERALD_CUST_PATH := emerald-cust

# Warn users you've included the cust package
$(warn "Compiling inline with the emerald-cust package.")

ifneq ($(LINEAGE_BUILD),)
$(warn "Adding OTA overrides for LineageOS")
# Set OTA property for emerald target.
ifeq ($(PRODUCT_DEVICE),emerald)
PRODUCT_PROPERTY_OVERRIDES += lineageos.updater.uri=https://raw.githubusercontent.com/teracube-mt6765-devs/releases/master/los11-emerald.json
else
PRODUCT_PROPERTY_OVERRIDES += lineageos.updater.uri=https://raw.githubusercontent.com/teracube-mt6765-devs/releases/master/los11-2e.json
endif
endif

# APN configuration
PRODUCT_COPY_FILES += \
    $(EMERALD_CUST_PATH)/telephony/apns-conf.xml:$(TARGET_COPY_OUT_PRODUCT)/etc/apns-conf.xml

# Apps
PRODUCT_PACKAGES += TeracubeCamera
