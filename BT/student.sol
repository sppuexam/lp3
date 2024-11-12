// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentDB {
    struct Student {
        string name;
        uint256 rollNo;
        string class;
    }

    Student[] private students;

    function addStudent(string memory name, uint256 rollNo, string memory class) public {
        students.push(Student(name, rollNo, class));
    }

    function getStudentById(uint256 id) public view returns (string memory, uint256, string memory) {
        require(id < students.length, "Student does not exist in database");
        return (students[id].name, students[id].rollNo, students[id].class);
    }

    function getTotalNumberOfStudents() public view returns (uint256) {
        return students.length;
    }

    // Function to search for a student by roll number
    function getStudentByRollNo(uint256 rollNo) public view returns (string memory, uint256, string memory) {
        for (uint256 i = 0; i < students.length; i++) {
            if (students[i].rollNo == rollNo) {
                return (students[i].name, students[i].rollNo, students[i].class);
            }
        }
        revert("Student with this roll number does not exist");
    }
 // Fallback function to handle incorrect calls or Ether transfers
    fallback() external payable {
        revert("Invalid function call or Ether transfer not allowed.");
    }

    // Receive function to accept Ether but prevent unintended usage
    receive() external payable {
        revert("This contract does not accept Ether.");
    }
}
