from flask import Flask, render_template

####
app = Flask(__name__)

# Define quiz data
quiz_data = [
    {
        "question": "What does DevSecOps primarily focus on?",
        "options": ["Development security", "DevOps processes", "Security collaboration", "Scalability"],
        "answer": "Development security",
    },
    {
        "question": "In DevSecOps, security is integrated into which phase of the software development lifecycle?",
        "options": ["Planning", "Coding", "Testing", "All of the above"],
        "answer": "All of the above",
    },
    {
        "question": "What is the goal of secure code analysis in DevSecOps?",
        "options": ["To speed up development", "To identify and fix security vulnerabilities early", "To improve user experience", "To reduce infrastructure costs"],
        "answer": "To identify and fix security vulnerabilities early",
    },
    {
        "question": "Which tool is used for scanning container images for security vulnerabilities?",
        "options": ["Jenkins", "SonarQube", "OWASP ZAP", "Clair"],
        "answer": "Clair",
    },
    {
        "question": "What is the practice of automatically identifying and responding to security incidents in DevSecOps?",
        "options": ["Incident Response", "Security Monitoring", "Continuous Integration", "Security Automation"],
        "answer": "Security Automation",
    },
    {
        "question": "What is the primary purpose of penetration testing in DevSecOps?",
        "options": ["To automate software deployments", "To monitor system performance", "To identify and fix security vulnerabilities", "To improve user experience"],
        "answer": "To identify and fix security vulnerabilities",
    },
    {
        "question": "Which DevSecOps principle emphasizes that security should be part of the development process from the beginning?",
        "options": ["Collaboration", "Automation", "Shift Left", "Scalability"],
        "answer": "Shift Left",
    },
    {
        "question": "What is a common security concern in containerized applications?",
        "options": ["Lack of automation", "Excessive resource usage", "Container escape vulnerabilities", "Code complexity"],
        "answer": "Container escape vulnerabilities",
    },
    {
        "question": "Which of the following is NOT a DevSecOps practice?",
        "options": ["Static code analysis", "Security training for developers", "Delaying security assessments", "Automated security testing"],
        "answer": "Delaying security assessments",
    },
    {
        "question": "What is the main goal of threat modeling in DevSecOps?",
        "options": ["Identifying and mitigating security risks", "Optimizing application performance", "Ensuring regulatory compliance", "Maximizing scalability"],
        "answer": "Identifying and mitigating security risks",
    },
    {
        "question": "What is the OWASP Top Ten?",
        "options": ["A list of the ten most critical DevSecOps tools", "A list of the ten most common security threats in web applications", "A set of guidelines for secure coding", "A DevSecOps best practices framework"],
        "answer": "A list of the ten most common security threats in web applications",
    },
    {
        "question": "What is the purpose of a Security Information and Event Management (SIEM) system in DevSecOps?",
        "options": ["To automate code deployment", "To monitor system performance", "To detect and respond to security incidents", "To improve collaboration among developers"],
        "answer": "To detect and respond to security incidents",
    },
    {
        "question": "Which type of testing focuses on simulating potential security attacks to identify vulnerabilities?",
        "options": ["Functional testing", "Load testing", "Security testing", "Usability testing"],
        "answer": "Security testing",
    },
    {
        "question": "What is the primary goal of DevSecOps in terms of security?",
        "options": ["To eliminate all security risks", "To shift security left in the development process", "To focus solely on reactive security measures", "To maximize system performance"],
        "answer": "To shift security left in the development process",
    },
    {
        "question": "What is the purpose of a security audit in DevSecOps?",
        "options": ["To automate code deployments", "To monitor user activity", "To assess compliance with security policies", "To enhance user experience"],
        "answer": "To assess compliance with security policies",
    },
    {
        "question": "What is the role of a DevSecOps engineer?",
        "options": ["To focus on development only", "To ensure infrastructure scalability", "To lead security efforts in development and operations", "To manage server configurations"],
        "answer": "To lead security efforts in development and operations",
    },
    {
        "question": "What is the primary goal of secure DevSecOps pipelines?",
        "options": ["To speed up software development", "To automate security assessments", "To improve infrastructure scalability", "To detect and remediate security vulnerabilities early"],
        "answer": "To detect and remediate security vulnerabilities early",
    },
    {
        "question": "Which security practice in DevSecOps focuses on protecting sensitive data from unauthorized access?",
        "options": ["Continuous monitoring", "Data encryption", "Containerization", "Load balancing"],
        "answer": "Data encryption",
    },
    {
        "question": "What is the benefit of security as code (SaC) in DevSecOps?",
        "options": ["Reducing the need for security testing", "Eliminating the need for DevOps practices", "Automating security controls and policies", "Improving system performance"],
        "answer": "Automating security controls and policies",
    },
    # Add more quiz questions here
]

@app.route('/')
def quiz():
    return render_template('index.html', quiz_data=quiz_data)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
