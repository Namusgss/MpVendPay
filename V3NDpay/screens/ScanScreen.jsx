import React, { useState, useEffect, useRef } from "react";
import { View, Text, StyleSheet, Alert } from "react-native";
import { Camera, CameraView } from "expo-camera";
import { useNavigation } from "@react-navigation/native";

const ScanScreen = ({ route }) => {
  const [hasPermission, setHasPermission] = useState(null);
  const [scanned, setScanned] = useState(false); // Ensures scanning happens once
  const navigation = useNavigation();
  const cameraRef = useRef(null);
  const { username } = route.params || { username: "Guest" };

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

      // Validate QR code identifier and amount
      if (parsedData.identifier === "VENDING_MACHINE") {
        if (!parsedData.transaction_id) {
          Alert.alert("Error", "Missing transaction ID in QR code.");
          return;
        }
        if (isNaN(parsedData.total_price) || parsedData.total_price <= 0) {
          Alert.alert("Error", "Invalid price in QR code.");
          return;
        }

        console.log(parsedData.transaction_id);
        // Navigate to PaymentScreen with transaction ID
        navigation.replace("PaymentScreen", {
          username: username, // Ensure username is passed correctly
          transactionId: parsedData.transaction_id, // Pass transaction ID
          productName: parsedData.productname,
          quantity: parsedData.quantity,
          amount: parsedData.total_price,
        });
        console.log(parsedData.transaction_id)
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
