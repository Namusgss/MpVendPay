import React from "react";
import { TouchableOpacity, Text, StyleSheet } from "react-native";
import { Ionicons } from "@expo/vector-icons";

const NavIcon = ({ name, icon, active, onPress }) => {
  return (
    <TouchableOpacity style={[styles.navIcon, active && styles.active]} onPress={onPress}>
      <Ionicons name={icon} size={28} color={active ? "#4CAF50" : "#888"} />
      <Text style={[styles.navIconText, active && styles.activeText]}>{name}</Text>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  navIcon: {
    alignItems: "center",
  },
  navIconText: {
    fontSize: 12,
    color: "#888",
  },
  active: {
    borderBottomWidth: 2,
    borderBottomColor: "#4CAF50",
  },
  activeText: {
    color: "#4CAF50",
  },
});

export default NavIcon;
