#include<string>
#include<iostream>
using namespace std;

class Student{
    public:
    //Non-parametarized constructor 
    Student(){
        cout<<("The constructor is called")<<endl;
    }

    //Parametrarized constructor 

    Student(string name, string faculty,int rollNo,int grade){
       this-> name=name;
         this->faculty=faculty;
         this->rollNo=rollNo;
         this->grade=grade;
    }

    string name;
    string faculty;
    int rollNo;
    int grade;

    void getInfo(){
    cout<<"Name:"<<name<<endl;
    cout<<"Grade :"<<grade<<endl;
    cout<<"Faculty :"<<faculty<<endl;
    cout<<"Roll No: "<<rollNo<<endl;

    }

};

class Account{
    private:
    double accNo;
    double balance;


    public:
    Account(){
        cout<<("Second constructor is called.")<<endl;
    }



    string name;
    string accType;

   
};



int main(){
    // Student st1;
    // st1.name="Ishan bartaula";
    // st1.rollNo=2;
    // // st1.faculty="Cosmology";
    // st1.grade=12;


    Student st1("Ishan bartaula","cosmology",2,12);

    st1.getInfo();
    Student st2;

    
    return 0;
}