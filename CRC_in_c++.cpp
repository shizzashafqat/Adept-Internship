//=================================================
// Shizza Fatima Shafqat 
// June 2024
// CRC.cpp
// This program implements the Cyclic Redundancy Check (CRC) algorithm in C++. 
//================================================= 

#include <iostream>
#include <string>

using namespace std;

// Function to compute the XOR of two binary strings
string xor1(string a, string b) {
    string result;
    for (int i = 0; i < a.size(); i++) {
        // Explicit if statement for clarity
        if ((a[i] == '1' && b[i] == '1') || (a[i] == '0' && b[i] == '0')) {
            result += '0'; // Both bits are the same, so XOR is 0
        } else {
            result += '1'; // Bits are different, so XOR is 1
        }
    }
    return result;
}

// Function to perform Modulo-2 division (long division using binary numbers but we are simply using XOR)
string mod2div(string dividend, string divisor) {
    int pick = divisor.size();
    string tmp = dividend.substr(0, pick);
    int n = dividend.size();

    while (pick < n) {
        if (tmp[0] == '1') {
            tmp = xor1(divisor, tmp) + dividend[pick];
        } else {
            tmp = xor1(string(pick, '0'), tmp) + dividend[pick];
        }
        pick += 1;
        tmp = tmp.substr(1); // Shift tmp
    }

    // Final step for the remaining bits
    if (tmp[0] == '1') {
        tmp = xor1(divisor, tmp);
    } else {
        tmp = xor1(string(pick, '0'), tmp);
    }

    return tmp.substr(1); // The remainder
}

// Function to encode data by appending the remainder of modular division at the end of data
void encodeData(string data, string key) {
    string appended_data = data + string(key.length() - 1, '0');
    string remainder = mod2div(appended_data, key);
    cout << "Encoded Data (Data + Remainder): " << data + remainder << endl;
}

// Function to check the received message
void receiver(string data, string key) {
    string remainder = mod2div(data, key);
    cout << "Final remainder at receiver: " << remainder << endl;
    if (remainder.find('1') != string::npos) { // Check if any '1's exist in the remainder
        cout << "There is some error in the data" << endl;
    } else {
        cout << "Correct message received" << endl;
    }
}

// Main function to drive the program
int main() {
    string data, key;
    cout << "Enter data (binary): ";
    cin >> data;
    cout << "Enter key (binary): ";
    cin >> key;

    cout << "Sender side..." << endl;
    encodeData(data, key);

    cout << "\nReceiver side..." << endl;
    string encodedData = data + mod2div(data + string(key.length() - 1, '0'), key);
    receiver(encodedData, key);

    return 0;
}
