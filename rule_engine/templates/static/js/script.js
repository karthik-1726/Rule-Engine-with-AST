function createRule() {
    const ruleInput = document.getElementById('ruleInput').value;
    const ruleError = document.getElementById('ruleError');

    if (!ruleInput) {
        ruleError.textContent = 'Please enter a rule';
        return;
    }

    ruleError.textContent = ''; // Clear any previous errors

    fetch('/create_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rule_string: ruleInput })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById('result').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error('Error:', error));
}

function combineRules() {
    const rulesInput = document.getElementById('rulesInput').value.trim().split('\n');
    const combineError = document.getElementById('combineError');

    if (rulesInput.length === 0 || rulesInput[0] === "") {
        combineError.textContent = 'Please enter at least one rule';
        return;
    }

    combineError.textContent = ''; // Clear any previous errors

    fetch('/combine_rules', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rules: rulesInput })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById('result').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error('Error:', error));
}

function evaluateRule() {
    const dataInput = document.getElementById('dataInput').value;
    const astInput = document.getElementById('astInput').value;
    const evaluateError = document.getElementById('evaluateError');

    if (!dataInput || !astInput) {
        evaluateError.textContent = 'Please enter both JSON data and AST JSON';
        return;
    }

    evaluateError.textContent = ''; // Clear any previous errors

    fetch('/evaluate_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data: JSON.parse(dataInput), ast: JSON.parse(astInput) })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById('result').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error('Error:', error));
}
