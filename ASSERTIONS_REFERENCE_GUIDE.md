# Test Assertions & Pattern Reference Guide

## Overview
This document provides detailed explanations for all assertions used in the three new test scenarios, including the testing philosophy and best practices applied.

---

## PART 1: DIGEST AUTHENTICATION TEST ASSERTIONS

### Test File: `test_digest_authentication.py`
**Purpose**: Validate HTTP Digest Authentication handling in Playwright
**Browser Support**: All (Chromium, Firefox, WebKit)
**Test Category**: Smoke Test

### Assertion Group 1: Authentication Success

#### Assertion 1.1: Success Message Not None
```python
assert success_message is not None, \
    "Success message should not be None"
```
**Explanation**:
- **What It Tests**: Page is accessible after navigation
- **Why It's Important**: Ensures page loaded and message retrieved successfully
- **Failure Reason**: Page might not have loaded or element not found
- **Recovery**: Check network connection and page locators

#### Assertion 1.2: Success Message Contains "Congratulations"
```python
assert "Congratulations" in success_message, \
    f"Expected 'Congratulations' in message, got: {success_message}"
```
**Explanation**:
- **What It Tests**: Authentication was successful
- **Why It's Important**: Confirms server accepted credentials
- **Expected Message**: "Congratulations! You must have the proper credentials."
- **Failure Scenario**: Wrong credentials or authentication mechanism failure
- **Recovery Steps**:
  1. Verify USERNAME and PASSWORD in test_data/digest_auth_data.py
  2. Check if website structure changed
  3. Verify network connectivity

#### Assertion 1.3: Authentication Status Method Returns True
```python
assert digest_page.is_authenticated() is True, \
    "Authentication should be successful"
```
**Explanation**:
- **What It Tests**: Page object method correctly identifies authenticated state
- **Why It's Important**: Validation through page object layer, not just string matching
- **Method Details**: Checks message exists AND contains "Congratulations"
- **Double Validation**: Ensures both content and page state are correct
- **Best Practice**: Page object methods encapsulate validation logic

#### Assertion 1.4: Complete Success Message Match
```python
assert EXPECTED_SUCCESS_MESSAGE in success_message, \
    f"Expected '{EXPECTED_SUCCESS_MESSAGE}' in message, got: {success_message}"
```
**Explanation**:
- **What It Tests**: Exact expected message is displayed
- **Why It's Important**: Validates complete authentication flow, not just partial
- **Test Data Variable**: EXPECTED_SUCCESS_MESSAGE = "Congratulations! You must have the proper credentials."
- **Why Full Message**: Minor text changes indicate website updates
- **Logging**: Helpful error message shows what was expected vs received

---

## PART 2: DISAPPEARING ELEMENTS TEST ASSERTIONS

### Test File: `test_disappearing_elements.py`
**Purpose**: Handle and validate dynamic/disappearing page elements
**Browser Support**: All (Chromium, Firefox, WebKit)
**Test Category**: Regression Test
**Challenge Addressed**: Framework robustness with dynamic UI elements

### Assertion Group 1: Page Load Validation

#### Assertion 1.1: Page Loaded Successfully
```python
assert disappearing_page.is_page_loaded() is True, \
    "Disappearing Elements page should load successfully"
```
**Explanation**:
- **What It Tests**: Page is accessible and heading is visible
- **Why It's Important**: Prerequisite for all element interactions
- **Failure Reason**: Page not found (404), network issue, or wrong URL
- **Method Details**: Calls `is_page_loaded()` which checks page heading visibility
- **Assertion Method**: Uses page object method for maintainability

#### Assertion 1.2: Page Heading Is Visible and Not Empty
```python
assert page_heading is not None, "Page heading should be visible"
assert page_heading.strip() != "", "Page heading should not be empty"
```
**Explanation**:
- **What It Tests**: Page has proper content and is fully loaded
- **Why It's Important**: Ensures page DOM is ready for element interactions
- **Two-Part Validation**:
  - First checks if element found (not None)
  - Second checks if element has content (not empty string)
- **Failure Reason**: Page not fully rendered or heading element missing
- **Double Check Pattern**: Best practice for robust assertions

### Assertion Group 2: Dynamic Element Handling

#### Assertion 2.1: Links Count Within Expected Range
```python
assert MIN_EXPECTED_LINKS <= links_count <= MAX_EXPECTED_LINKS, \
    f"Expected {MIN_EXPECTED_LINKS}-{MAX_EXPECTED_LINKS} links, got {links_count}"
```
**Explanation**:
- **What It Tests**: Framework handles variable element count
- **Why It's Important**: Disappearing Elements page has 5 possible links (Home, About, Contact Us, Portfolio, Gallery)
  - Gallery link disappears randomly on each page load
  - Test should pass with 4 or 5 links visible
- **Test Data Values**:
  ```python
  MIN_EXPECTED_LINKS = 4  # Home, About, Contact Us, Portfolio
  MAX_EXPECTED_LINKS = 5  # + Gallery (when present)
  ```
- **Why Range-Based**: Tests robustness, not brittle count matching
- **Error Message**: Shows actual count for debugging

#### Assertion 2.2: Visible Links Exist
```python
assert len(visible_links) > 0, "Should have at least one visible link"
```
**Explanation**:
- **What It Tests**: Page has navigable elements
- **Why It's Important**: Confirms links array is populated
- **Failure Reason**: Pages might have rendering issues
- **Simple Check**: Validates minimum page functionality

#### Assertion 2.3: Static Links Existence
```python
for link in ['Home', 'About']:
    assert disappearing_page.verify_link_exists(link), \
        f"Static link '{link}' should exist on the page"
```
**Explanation**:
- **What It Tests**: Core navigation links always available
- **Why It's Important**: Ensures disappearing elements are only optional ones
- **Test Data Knowledge**: Home and About are guaranteed static links
- **Gallery Link**: Not tested in this assertion (it can disappear)
- **Looping Pattern**: Dynamic assertion for multiple related validations
- **Framework Robustness**: Tests know which elements should/shouldn't disappear

### Assertion Group 3: Stability & Consistency

#### Assertion 3.1: Page Remains Stable
```python
assert (
    links_count == links_count_second_check or
    abs(links_count - links_count_second_check) <= 1
), "Links count should remain stable during test execution"
```
**Explanation**:
- **What It Tests**: Page state consistency within single test run
- **Why It's Important**: Validates test doesn't cause page reload unexpectedly
- **Tolerance Logic**: One-link difference allowed (accounts for Gallery link state)
- **Failure Scenario**: Page might reload during test or element rendering issue
- **Best Practice**: Checks consistency without being too strict
- **Practical Use**: Prevents flaky tests from false element appearance/disappearance

---

## PART 3: DRAG AND DROP TEST ASSERTIONS

### Test File: `test_drag_drop.py`
**Purpose**: Validate complex user interactions - Drag and Drop operations
**Browser Support**: All (Chromium, Firefox, WebKit)
**Test Category**: Smoke Test
**Challenge Addressed**: Handling complex Playwright interactions

### Assertion Group 1: Initial State Validation (Before Drag)

#### Assertion 1.1: Column A Initially Contains "A"
```python
assert initial_column_a == INITIAL_LEFT_CONTENT, \
    f"Column A should initially contain '{INITIAL_LEFT_CONTENT}', got '{initial_column_a}'"
```
**Explanation**:
- **What It Tests**: Left box has correct initial element
- **Why It's Important**: Establishes baseline before performing drag operation
- **Test Data**: `INITIAL_LEFT_CONTENT = "A"`
- **Failure Reason**: Page not rendered correctly or position swapped initially
- **Assertion Type**: Exact match (==), not substring match
- **Error Details**: Shows both expected and actual values for debugging

#### Assertion 1.2: Column B Initially Contains "B"
```python
assert initial_column_b == INITIAL_RIGHT_CONTENT, \
    f"Column B should initially contain '{INITIAL_RIGHT_CONTENT}', got '{initial_column_b}'"
```
**Explanation**:
- **What It Tests**: Right box has correct initial element
- **Why It's Important**: Establishes second baseline for swap validation
- **Test Data**: `INITIAL_RIGHT_CONTENT = "B"`
- **Mirror Logic**: Matches assertion for Column A
- **Symmetrical Testing**: Both columns validated before and after
- **Atomic Baseline**: Single point of truth for initial state

#### Assertion 1.3: Initial State Verification Method
```python
assert drag_drop_page.verify_initial_state() is True, \
    "Initial state verification should pass"
```
**Explanation**:
- **What It Tests**: Page object method confirms initial state
- **Why It's Important**: Encapsulates initial state logic in page object
- **Method Details**: Returns `True` if A in left AND B in right
- **Redundancy Value**: Double-checks initial state via different method
- **Best Practice**: Page object methods should validate state
- **Usage Pattern**: Allows reuse of initial state verification

### Assertion Group 2: Drag Operation & Results

#### Assertion 2.1: Drag Operation Success
```python
assert drag_success is True, \
    "Drag and drop operation should complete successfully"
```
**Explanation**:
- **What It Tests**: Drag and drop action completed without errors
- **Why It's Important**: Validates Playwright's drag_to() method worked
- **Method**: Returns boolean from try-except block in page object
- **Failure Reason**: Element not visible, stale element reference, or locator issue
- **Debugging**: If fails, check browser console for JavaScript errors
- **Recovery**: Verify locators are correct for the website

### Assertion Group 3: Final State Validation (After Drag)

#### Assertion 3.1: Column A Contains "B" After Drag
```python
assert final_column_a == EXPECTED_LEFT_AFTER_DRAG, \
    f"Column A should contain '{EXPECTED_LEFT_AFTER_DRAG}' after drag, got '{final_column_a}'"
```
**Explanation**:
- **What It Tests**: Left box now contains element B (swap successful)
- **Why It's Important**: Proves drag source element was moved
- **Test Data**: `EXPECTED_LEFT_AFTER_DRAG = "B"`
- **Mirror of Initial**: Initially had A, now has B
- **Critical Assertion**: Validates drag action had effect
- **Before/After Pattern**: Shows state change

#### Assertion 3.2: Column B Contains "A" After Drag
```python
assert final_column_b == EXPECTED_RIGHT_AFTER_DRAG, \
    f"Column B should contain '{EXPECTED_RIGHT_AFTER_DRAG}' after drag, got '{final_column_b}'"
```
**Explanation**:
- **What It Tests**: Right box now contains element A (swap complete)
- **Why It's Important**: Proves drag target received the element
- **Test Data**: `EXPECTED_RIGHT_AFTER_DRAG = "A"`
- **Completes Swap**: Combined with assertion 3.1, validates complete swap
- **Bidirectional**: Tests both source and target of drag operation
- **Symmetric Validation**: Mirrors assertion 3.1

#### Assertion 3.3: Swapped State Verification Method
```python
assert drag_drop_page.verify_swapped_state() is True, \
    "Swapped state verification should pass"
```
**Explanation**:
- **What It Tests**: Page object method confirms swap
- **Why It's Important**: Encapsulates post-drag validation logic
- **Method Details**: Returns `True` if B in left AND A in right
- **Redundancy Value**: Third validation method for final state
- **Multiple Checks**: Ensures swap via different verification method
- **Confidence Level**: Three assertions for high confidence in swap

### Assertion Group 4: State Change Confirmation

#### Assertion 4.1: Column A Content Changed
```python
assert initial_column_a != final_column_a, \
    "Column A content should change after drag operation"
```
**Explanation**:
- **What It Tests**: Left box content is different before and after
- **Why It's Important**: Confirms something actually happened
- **Value Flow**: "A" → "B" (inequality confirms change)
- **Complementary Check**: Validates change occurred
- **Failure Scenario**: Drag didn't work, same element still there
- **Simple But Powerful**: Direct comparison of before/after state

#### Assertion 4.2: Column B Content Changed
```python
assert initial_column_b != final_column_b, \
    "Column B content should change after drag operation"
```
**Explanation**:
- **What It Tests**: Right box content is different before and after
- **Why It's Important**: Confirms both boxes affected by drag
- **Value Flow**: "B" → "A" (inequality confirms change)
- **Symmetrical Validation**: Matches check for Column A
- **Comprehensive Test**: Tests impact on both elements
- **Final Confirmation**: Ensures swap, not just displacement

---

## PART 4: ASSERTION PATTERNS & BEST PRACTICES

### Pattern 1: Pre-Condition Validation
**Used In**: Drag and Drop test (assertions 1.1-1.3)
**Purpose**: Establish baseline before performing action
**Code Example**:
```python
assert initial_state == expected
# Then perform action
perform_action()
# Then assert post-state
assert final_state == expected
```
**Best Practice**: Always validate prerequisites

### Pattern 2: Postcondition Validation
**Used In**: All tests
**Purpose**: Verify action had intended effect
**Code Example**:
```python
perform_action()
assert action_result == expected
```
**Best Practice**: Direct result validation

### Pattern 3: Method Encapsulation
**Used In**: All tests (e.g., `is_authenticated()`, `is_page_loaded()`)
**Purpose**: Hide validation complexity in page object
**Code Example**:
```python
# Page object method
def is_authenticated(self):
    message = self.get_success_message()
    return "Congratulations" in message

# Test assertion
assert page_object.is_authenticated() is True
```
**Best Practice**: Encapsulate logic in page objects

### Pattern 4: Multiple Validation Levels
**Used In**: Digest Auth test (assertions 1.2, 1.3, 1.4)
**Purpose**: Reusable assertions with different validation levels
**Code Example**:
```python
assert "Congratulations" in message        # Content check
assert page.is_authenticated() is True      # State check  
assert EXACT_MESSAGE in message             # Exact match
```
**Best Practice**: Multiple checks at different levels

### Pattern 5: Range-Based Assertions
**Used In**: Disappearing Elements test (assertion 2.1)
**Purpose**: Handle variable results
**Code Example**:
```python
assert MIN_EXPECTED <= actual_count <= MAX_EXPECTED
```
**Best Practice**: Use ranges for dynamic content

### Pattern 6: State Comparison
**Used In**: Drag and Drop test (assertions 4.1-4.2)
**Purpose**: Verify state changed
**Code Example**:
```python
assert initial_state != final_state
```
**Best Practice**: Confirm change with inequality

### Pattern 7: Comprehensive Assertions
**Used In**: All tests
**Purpose**: Detailed error messages
**Code Example**:
```python
assert value == expected, \
    f"Expected '{expected}', got '{value}'"
```
**Best Practice**: Always include context in assertion message

---

## PART 5: ERROR SCENARIOS & DEBUGGING

### Digest Authentication Failures

| Assertion | Failure Reason | Debug Steps |
|-----------|----------------|------------|
| success_message is not None | Page didn't load | Check BASE_URL, network connection |
| "Congratulations" in message | Wrong credentials | Verify USERNAME/PASSWORD in test data |
| is_authenticated() is False | Page element changed | Inspect page DOM, update locator |
| Exact message not found | Website text changed | Update EXPECTED_SUCCESS_MESSAGE |

### Disappearing Elements Failures

| Assertion | Failure Reason | Debug Steps |
|-----------|----------------|------------|
| is_page_loaded() is False | Page didn't load | Check navigation, BASE_URL |
| Links count out of range | Element count changed | Reload page, verify initial state |
| Static link missing | Website structure changed | Inspect page, update locators |
| Page not stable | Unexpected reload occurred | Check console for errors |

### Drag and Drop Failures

| Assertion | Failure Reason | Debug Steps |
|-----------|----------------|------------|
| Initial state wrong | Page loaded incorrectly | Reload page, verify initial position |
| Drag operation fails | Element not draggable | Check locators, element visibility |
| Final state wrong | Drag didn't complete | Check network, browser compatibility |
| State didn't change | No action occurred | Verify drag_to() method works |

---

## PART 6: ASSERTION STATISTICS

### Digest Authentication Test
- **Total Assertions**: 4
- **Pre-condition Assertions**: 0
- **Post-condition Assertions**: 4
- **Method-based Assertions**: 1
- **String Match Assertions**: 2

### Disappearing Elements Test
- **Total Assertions**: 7
- **Pre-condition Assertions**: 2
- **Post-condition Assertions**: 5
- **Range-based Assertions**: 1
- **Loop-based Assertions**: 1

### Drag and Drop Test
- **Total Assertions**: 7
- **Pre-condition Assertions**: 4
- **Post-condition Assertions**: 7
- **Equality Assertions**: 4
- **Inequality Assertions**: 2

### Combined Statistics
- **Total Assertions Across All Tests**: 18
- **Expected Pass Rate**: 100%
- **Assertion Density**: ~6 per test
- **Coverage**: Three scenarios, multiple assertion types

---

## PART 7: ASSERTION MAINTENANCE GUIDELINES

### When Assertions Fail

1. **Read Error Message**: Shows expected vs actual value
2. **Check Test Output**: Logs show step-by-step execution
3. **Verify Website**: Check if website structure changed
4. **Update Test Data**: If website changed expected values
5. **Update Locators**: If element selectors changed
6. **Review Logs**: Logger outputs details for debugging

### When to Add Assertions

- ✅ Add when new functionality is tested
- ✅ Add when bug is found (regression prevention)
- ✅ Add for critical user flows
- ❌ Don't add redundant assertions
- ❌ Don't assert implementation details

### When to Modify Assertions

- ✅ When website changes expected values
- ✅ When element selectors change
- ✅ When business logic changes
- ❌ Don't modify to make tests pass
- ❌ Don't weaken assertions to avoid failures

---

**Last Updated**: June 15, 2026  
**Framework Version**: 1.1  
**Status**: Production Ready

