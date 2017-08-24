# This image extends arago-console-image image with additional
# recipes necessary for smart clock

require ../../../meta-arago/meta-arago-distro/recipes-core/images/arago-console-image.bb

IMAGE_INSTALL += "\
	dropbear \
	packagegroup-arago-tisdk-connectivity \
	python \
	python-pip \
	python-evdev \
	u-boot-ti-staging \
	packagegroup-arago-qte \
	ntpdate \
	evtest \
	ti-sgx-ddk-km  \
	ti-sgx-ddk-um  \
	digital-clock \
"

export IMAGE_BASENAME = "core-image-clock"
