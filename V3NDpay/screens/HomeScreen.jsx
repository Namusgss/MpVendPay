import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Image,
  Alert,
  Modal,
} from "react-native";
import { Ionicons, FontAwesome5 } from "@expo/vector-icons";
import { Camera } from "expo-camera";

const HomeScreen = () => {
  const [userName, setUserName] = useState(""); // State to store the user's name
  const [hasPermission, setHasPermission] = useState(null); // Permission for the camera
  const [scannerVisible, setScannerVisible] = useState(false); // Modal visibility

  // Simulating fetching the name (e.g., from an API or local storage)
  useEffect(() => {
    const fetchUserName = async () => {
      const nameFromVendpayId = ""; // Replace this with real logic to get the name
      setUserName(nameFromVendpayId);
    };

    fetchUserName();

    // Request permission for the camera
    const getCameraPermission = async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      setHasPermission(status === "granted");
    };

    getCameraPermission();
  }, []);

  if (hasPermission === null) {
    return <Text>Requesting for camera permissions...</Text>;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  return (
    <View style={styles.container}>
      {/* Top Header */}
      <View style={styles.header}>
        <Text style={styles.time}>9:49</Text>
        <View style={styles.profile}>
          <Image
            source={{ uri: "https://via.placeholder.com/50" }} // Replace with the actual profile image
            style={styles.profileImage}
          />
          <Text style={styles.greeting}>Hi, {userName}</Text>
          <Ionicons name="checkmark-circle" size={16} color="green" />
        </View>
        <View style={styles.headerIcons}>
          <Ionicons name="search" size={24} color="#fff" />
          <Ionicons name="notifications-outline" size={24} color="#fff" />
          <Ionicons name="chatbubble-outline" size={24} color="#fff" />
        </View>
      </View>

      {/* Features Section */}
      <ScrollView>
        <View style={styles.featuresSection}>
          <View style={styles.featureRow}>
            <FeatureIcon name="Load Money" icon="wallet" />
          </View>
          <Text style={styles.sectionTitle}>Utility & Bill Payments</Text>
          <View style={styles.featureRow}>
            <FeatureIcon name="Live Inventory" icon="mobile" />
          </View>
        </View>

        {/* QR Code Scanner Button */}
        <TouchableOpacity
          style={styles.qrScannerButton}
          onPress={() => setScannerVisible(true)}
        >
          <Ionicons name="qr-code-outline" size={32} color="#fff" />
          <Text style={styles.qrScannerText}>Open Camera</Text>
        </TouchableOpacity>
      </ScrollView>

      {/* Camera Modal */}
      <Modal visible={scannerVisible} animationType="slide">
        <View style={styles.scannerContainer}>
          <Camera style={StyleSheet.absoluteFillObject} />
          <TouchableOpacity
            style={styles.closeScannerButton}
            onPress={() => setScannerVisible(false)}
          >
            <Text style={styles.closeScannerText}>Close</Text>
          </TouchableOpacity>
        </View>
      </Modal>

      {/* Bottom Navigation */}
      <View style={styles.bottomNav}>
        <NavIcon name="Home" icon="home" active />
        <NavIcon name="Statement" icon="document-text" />
        <NavIcon name="Support" icon="help-circle" />
        <NavIcon name="More" icon="apps" />
      </View>
    </View>
  );
};

const FeatureIcon = ({ name, icon }) => (
  <TouchableOpacity style={styles.featureIcon}>
    <FontAwesome5 name={icon} size={24} color="#4CAF50" />
    <Text style={styles.featureText}>{name}</Text>
  </TouchableOpacity>
);

const NavIcon = ({ name, icon, active }) => (
  <TouchableOpacity style={styles.navIcon}>
    <Ionicons name={icon} size={28} color={active ? "#4CAF50" : "#aaa"} />
    <Text style={[styles.navText, active && { color: "#4CAF50" }]}>{name}</Text>
  </TouchableOpacity>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
  header: {
    backgroundColor: "#4CAF50",
    paddingHorizontal: 20,
    paddingTop: 50,
    paddingBottom: 15,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  time: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "bold",
  },
  profile: {
    flexDirection: "row",
    alignItems: "center",
  },
  profileImage: {
    width: 40,
    height: 40,
    borderRadius: 20,
    marginRight: 10,
  },
  greeting: {
    color: "#fff",
    fontSize: 16,
    marginRight: 5,
  },
  headerIcons: {
    flexDirection: "row",
    gap: 10,
  },
  featuresSection: {
    paddingHorizontal: 20,
    marginBottom: 20,
  },
  featureRow: {
    flexDirection: "row",
    justifyContent: "flex-start",
    marginBottom: 20,
  },
  featureIcon: {
    alignItems: "center",
    marginRight: 30,
  },
  featureText: {
    fontSize: 12,
    color: "#555",
    marginTop: 5,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: "bold",
    marginBottom: 10,
  },
  qrScannerButton: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#4CAF50",
    padding: 10,
    margin: 20,
    borderRadius: 10,
  },
  qrScannerText: {
    color: "#fff",
    fontSize: 16,
    marginLeft: 10,
  },
  scannerContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  closeScannerButton: {
    position: "absolute",
    bottom: 50,
    backgroundColor: "#fff",
    padding: 10,
    borderRadius: 20,
  },
  closeScannerText: {
    color: "#4CAF50",
    fontWeight: "bold",
  },
  bottomNav: {
    flexDirection: "row",
    justifyContent: "space-around",
    paddingVertical: 10,
    backgroundColor: "#fff",
    borderTopWidth: 1,
    borderColor: "#eee",
  },
  navIcon: {
    alignItems: "center",
  },
  navText: {
    fontSize: 12,
    color: "#aaa",
  },
});

export default HomeScreen;
