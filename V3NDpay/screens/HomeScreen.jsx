import React from "react";
import { View, Text, StyleSheet, ScrollView } from "react-native";

const HomeScreen = () => {
  return (
    <View style={styles.container}>
      <ScrollView>
        <Text style={styles.welcomeText}>Welcome to Home Screen</Text>
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    justifyContent: "center",
    alignItems: "center",
  },
  welcomeText: {
    fontSize: 20,
    fontWeight: "bold",
  },
});

export default HomeScreen;
