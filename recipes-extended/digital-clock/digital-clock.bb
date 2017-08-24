SUMMARY = "digital clock app"

LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://${WORKDIR}/COPYING.GPL;md5=751419260aa954499f7abaabaa882bbe"

PR = "r0"

RDEPENDS_${PN} += " \
	qtbase \
	qtdeclarative \
	ti-sgx-ddk-um \
"

SRC_URI = "file://qt-clock \
           file://alarm.wav \
           file://digital-clock.py \
           file://dot.profile \
           file://hostapdclock.conf \
           file://COPYING.GPL"

do_compile() {
	:
}

do_install() {
	install -d ${D}/bin
	install -m 0755 ${WORKDIR}/qt-clock ${D}/bin/qt-clock
	install -m 0755 ${WORKDIR}/alarm.wav ${D}/bin/alarm.wav
	install -m 0755 ${WORKDIR}/digital-clock.py ${D}/bin/digital-clock.py

	install -d ${D}/etc
	install -m 0755 ${WORKDIR}/hostapdclock.conf ${D}/etc/hostapdclock.conf

	install -d ${D}/home/root
	install -m 0755 ${WORKDIR}/dot.profile ${D}/home/root/.profile
}

FILES_${PN} += "/bin/ /etc/ /home/root/"

S = "${WORKDIR}/digital-clock${PR}"
