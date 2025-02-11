// AboutUsScreen.js
import React from "react";
import { View, Text, StyleSheet, Button } from "react-native";

const AboutUsScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>About Us</Text>
      <Text style={styles.description}>
        This is a vending machine app developed by Suman Bhandari.
        The goal of this app is to provide a seamless and efficient way to
        purchase products using online payment methods.
      </Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#E8F5E9",
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#2E7D32",
    marginBottom: 10,
  },
  description: {
    fontSize: 16,
    color: "#555",
    textAlign: "center",
    marginTop: 10,
  },
});

export default AboutUsScreen;
