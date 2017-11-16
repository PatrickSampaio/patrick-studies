##Unite Testing

What are Mocks

- Stubs
	Provide a canned response to method calls

- Spy
	Normal object that behavior normal, except when an condition is met

- Mocks
	Verifies behavior

#What kind of problems that Mock solves

1 - Eliminate Dependencies
2 - Tests methods that have no return value
3 - Error handling

On python, decorators stack. Then you can have multiple decortartos `@mock.path`,
but them are represented in the inverse on the test parameters. You can use 
`@mock.Multiple`

`mock_send_email.call_args_list`, arguments list that the mock recieved

Mock an bultin method
`@patch("__bultin__.open")
`mock_file = Mock()`
`mock_file.open.return_value = '{"foo":"bar"}'`
Then:
`mock_open.return_value = mock_file`

Mock an error, to see error handling
`@path("__bultin__.open")
`mock_open.side_effect = IOError`

Takes Aways
1 - Mocking makes writing unit tests simpler
2 - Help to eliminate dependencies
3 - Mock helps to verifies behavior
4 - Mock helps to verifies error handling
