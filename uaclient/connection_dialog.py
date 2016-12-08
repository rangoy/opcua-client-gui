from PyQt5.QtWidgets import QDialog, QFileDialog

from uaclient.connection_ui import Ui_ConnectionDialog


class ConnectionDialog(QDialog):
    def __init__(self, parent, uri):
        QDialog.__init__(self)
        self.ui = Ui_ConnectionDialog()
        self.ui.setupUi(self)

        self.uaclient = parent.uaclient
        self.uri = uri
        
        self.ui.modeComboBox.addItem("None")
        self.ui.modeComboBox.addItem("Sign")
        self.ui.modeComboBox.addItem("SignAndEncrypt")

        self.ui.policyComboBox.addItem("None")
        self.ui.policyComboBox.addItem("Basic128Rsa15")
        self.ui.policyComboBox.addItem("Basic256")

        self.ui.closeButton.clicked.connect(self.accept)
        self.ui.certificateButton.clicked.connect(self.get_certificate)
        self.ui.privateKeyButton.clicked.connect(self.get_private_key)

    @property
    def security_mode(self):
        return self.ui.modeComboBox.currentText()

    @security_mode.setter
    def security_mode(self, value):
        self.ui.modeComboBox.setCurrentText(value)

    @property
    def security_policy(self):
        return self.ui.policyComboBox.currentText()

    @security_policy.setter
    def security_policy(self, value):
        self.ui.policyComboBox.setCurrentText(value)

    @property
    def certificate_path(self):
        return self.ui.certificateLabel.text()

    @certificate_path.setter
    def certificate_path(self, value):
        self.ui.certificateLabel.setText(value)

    @property
    def private_key_path(self):
        return self.ui.privateKeyLabel.text()

    @private_key_path.setter
    def private_key_path(self, value):
        self.ui.privateKeyLabel.setText(value)

    def get_certificate(self):
        path, ok = QFileDialog.getOpenFileName(self, "Select certificate", self.certificate_path, "Certificate (*.der)")
        if ok:
            self.ui.certificateLabel.setText(path)

    def get_private_key(self):
        path, ok = QFileDialog.getOpenFileName(self, "Select private key", self.private_key_path, "Private key (*.pem)")
        if ok:
            self.ui.privateKeyLabel.setText(path)


