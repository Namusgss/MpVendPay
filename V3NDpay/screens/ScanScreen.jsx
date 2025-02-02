import React, { useState, useEffect, useRef } from "react";
import { View, Text, StyleSheet, Alert } from "react-native";
import { Camera, CameraView } from "expo-camera";
import { useNavigation } from "@react-navigation/native";

const ScanScreen = () => {
  const [hasPermission, setHasPermission] = useState(null);
  const [scanned, setScanned] = useState(false); // Ensures scanning happens once
  const navigation = useNavigation();
  const cameraRef = useRef(null);

  // Request camera permission
  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      setHasPermission(status === "granted");
    })();
  }, []);

  // Handle QR Code scan
  const handleBarCodeScanned = ({ data }) => {
    if (scanned) return; // Prevents multiple scans
    setScanned(true); // Lock scanning after one scan

    try {
      const parsedData = JSON.parse(data);

      // Validate QR code identifier
      if (parsedData.identifier === "VENDING_MACHINE") {
        navigation.replace("PaymentScreen", {
          productName: parsedData.productName,
          quantity: parsedData.quantity,
          amount: parsedData.amount,
        });
      } else {
        Alert.alert("Invalid QR Code", "This QR code is not from a vending machine.");
        setTimeout(() => setScanned(false), 2000); // Allow rescanning after 2 seconds
      }
    } catch (error) {
      Alert.alert("Error", "Invalid QR code format.");
      setTimeout(() => setScanned(false), 2000); // Allow rescanning after 2 seconds
    }
  };

  if (hasPermission === null) {
    return <Text>Requesting camera permission...</Text>;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Scan Vending Machine QR Code</Text>
      <View style={styles.cameraContainer}>
        <CameraView
          ref={cameraRef}
          onBarcodeScanned={scanned ? undefined : handleBarCodeScanned}
          barcodeScannerSettings={{ barcodeTypes: ["qr"] }}
          style={StyleSheet.absoluteFillObject}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#E8F5E9",
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
  },
  title: {
    fontSize: 22,
    fontWeight: "bold",
    color: "#2E7D32",
    marginBottom: 20,
  },
  cameraContainer: {
    width: "80%",
    aspectRatio: 1,
    overflow: "hidden",
    borderRadius: 10,
    backgroundColor: "#000",
  },
});

export default ScanScreen;