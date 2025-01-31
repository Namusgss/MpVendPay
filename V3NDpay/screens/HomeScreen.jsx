import React, { useState, useEffect, useRef } from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Alert,
  Modal,
} from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { Camera } from "expo-camera";
import * as MediaLibrary from "expo-media-library";

const HomeScreen = () => {
  const [hasPermission, setHasPermission] = useState(null);
  const [cameraVisible, setCameraVisible] = useState(false);
  const [scanned, setScanned] = useState(false);
  const [scanData, setScanData] = useState(null);
  const cameraRef = useRef(null);

  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      const mediaStatus = await MediaLibrary.requestPermissionsAsync();
      setHasPermission(status === "granted" && mediaStatus.status === "granted");
    })();
  }, []);

  const takePicture = async () => {
    if (cameraRef.current) {
      const photo = await cameraRef.current.takePictureAsync();
      await MediaLibrary.saveToLibraryAsync(photo.uri);
      Alert.alert("Photo Saved", "The photo has been saved to your gallery.");
    }
  };

  const handleBarCodeScanned = ({ type, data }) => {
    setScanned(true);
    setScanData(data);
    Alert.alert("QR Code Scanned", `Data: ${data}`);
  };

  if (hasPermission === null) {
    return <Text>Requesting for camera permissions...</Text>;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  return (
    <View style={styles.container}>
      <ScrollView>
        <TouchableOpacity
          style={styles.cameraButton}
          onPress={() => setCameraVisible(true)}
        >
          <Ionicons name="camera" size={32} color="#fff" />
          <Text style={styles.cameraText}>Open Camera</Text>
        </TouchableOpacity>
      </ScrollView>

      <Modal visible={cameraVisible} animationType="slide">
        <View style={styles.cameraContainer}>
          <Camera
            ref={cameraRef}
            style={StyleSheet.absoluteFillObject}
            onBarCodeScanned={scanned ? undefined : handleBarCodeScanned}
            barCodeScannerSettings={{
              barCodeTypes: [Camera.Constants.BarCodeTypes.QR],
            }}
          />
          {scanned && (
            <TouchableOpacity
              style={styles.rescanButton}
              onPress={() => setScanned(false)}
            >
              <Text style={styles.rescanText}>Scan Again</Text>
            </TouchableOpacity>
          )}
          <TouchableOpacity style={styles.captureButton} onPress={takePicture}>
            <Text style={styles.captureText}>Capture</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.closeButton}
            onPress={() => setCameraVisible(false)}
          >
            <Text style={styles.closeText}>Close</Text>
          </TouchableOpacity>
        </View>
      </Modal>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
  cameraButton: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#4CAF50",
    padding: 10,
    margin: 20,
    borderRadius: 10,
  },
  cameraText: {
    color: "#fff",
    fontSize: 16,
    marginLeft: 10,
  },
  cameraContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  captureButton: {
    position: "absolute",
    bottom: 100,
    backgroundColor: "#4CAF50",
    padding: 10,
    borderRadius: 20,
  },
  captureText: {
    color: "#fff",
    fontWeight: "bold",
  },
  rescanButton: {
    position: "absolute",
    bottom: 150,
    backgroundColor: "#4CAF50",
    padding: 10,
    borderRadius: 20,
  },
  rescanText: {
    color: "#fff",
    fontWeight: "bold",
  },
  closeButton: {
    position: "absolute",
    bottom: 50,
    backgroundColor: "#fff",
    padding: 10,
    borderRadius: 20,
  },
  closeText: {
    color: "#4CAF50",
    fontWeight: "bold",
  },
});

export default HomeScreen;
