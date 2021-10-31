#include<iostream>
#include<string>
using namespace std;
int main(){

	std::string alphabet{"ABCDEFGHIJKLMNOPQRSTUVWXYZ"};
	//cout<<alphabet[1]<<endl;
	std::string key{"ZYXWVUTSRQPONMLKJIHGFEDCBA"};
	//cout<<key[1]<<endl;	

	cout<<"Enter you message"<<endl;
	std::string s1{};
	std::string s2{};
	getline(cin, s1);//s1 has BCAabc
	//cout<<"You have entered "<<s1<<endl;
	int temp = 0;
	char val {};
	cout<<"Decrypting the message:....."<<endl;
	// for (size_t i = 0; i < s1.length(); ++i)
	// {
	// 		val = s1[i];
	// 		if(val == string::npos){
	// 			cout<<" ";
	// 		}else{
	// 			

	// 		}
			
			
		
		
	// 	// cout<<s1[i];	
	// }
	for (char c : s1){

		size_t position = alphabet.find(c);
		if(position != string::npos){
			char newVal = key[position];
			s2 += newVal;

		}else{
			s2 += c;
		}
	}

	cout<<"The encrypted message is "<<s2<<endl;


}
