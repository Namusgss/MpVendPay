
import React, { useState } from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

import LoginScreen from "./screens/LoginScreen";
import SignUpScreen from "./screens/SignUpScreen";
import HomeScreen from "./screens/HomeScreen";
import PaymentScreen from "./screens/PaymentScreen";
import ScanScreen from "./screens/ScanScreen";
import StatementScreen from "./screens/StatementScreen";
import SupportScreen from "./screens/SupportScreen";
import MoreScreen from "./screens/MoreScreen";
import AboutUsScreen from "./screens/AboutUsScreen"; 
import BrowseInventoryScreen from "./screens/BrowseInventoryScreen"; 

const Stack = createStackNavigator();

export default function App() {
  // Global state for storing user credentials
  const [userCredentials, setUserCredentials] = useState(null);

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="SignUp">
        <Stack.Screen 
          name="SignUp" 
          component={SignUpScreen} 
          options={{ headerShown: false }} 
        />
        <Stack.Screen 
          name="Login" 
          component={LoginScreen} 
          options={{ headerShown: false }} 
        />
        <Stack.Screen 
          name="Home" 
          component={HomeScreen} 
          options={{ headerShown: false }} 
        />
        <Stack.Screen 
          name="ScanToPay" 
          component={ScanScreen} 
          options={{ headerShown: false }} 
        />
        <Stack.Screen 
          name="PaymentScreen" 
          component={PaymentScreen} 
          options={{ headerShown: false }} 
        />
        <Stack.Screen 
          name="Statement" 
          component={StatementScreen} 
          initialParams={{ username: userCredentials?.username }} 
        />
        <Stack.Screen 
          name="Support" 
          component={SupportScreen} 
          initialParams={{ username: userCredentials?.username }} 
        />
        <Stack.Screen 
          name="More" 
          component={MoreScreen} 
          initialParams={{ username: userCredentials?.username }} 
        />
        <Stack.Screen 
          name="AboutUs" 
          component={AboutUsScreen} 
          initialParams={{ username: userCredentials?.username }} 
        />
        {/* Browse Inventory Screen */}
        <Stack.Screen 
        name="BrowseInventory" component={BrowseInventoryScreen}
        initialParams={{ username: userCredentials?.username }} 
        />
      
      </Stack.Navigator>
    </NavigationContainer>
  );
}
