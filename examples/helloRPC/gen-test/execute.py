# Test helloRPC

# target (for quark install --blah), server command, client command, output pattern, nocmp
# Java's nocmp is True because mvn and logging stick timestamps in the
# output by default, breaking full-file comparisons.
targets = (
    ("java", "mvn exec:java -Dexec.mainClass=helloRPC.HelloRPCServer",
     "mvn exec:java -Dexec.mainClass=helloRPC.HelloRPCClient", "Java", True),
    ("python", "python pyserver.py", "python pyclient.py", "Python", False),
    ("javascript", "node jsserver.js", "node jsclient.js", "JavaScript", False),
    ("ruby", "ruby rbserver.rb", "ruby rbclient.rb", "Ruby", False)
)

# Install everything all-at-once. This will generate the .qc files.
install_all = helpers.quark_install("hello.q")

# Install everything one-at-a-time to capture individual output for docs
for target, server_cmd, client_cmd, pattern, nocmp in targets:
    installation = helpers.quark_install("--%s hello.q" % target)

# Extra step for Java
java_compile = helpers.mvn("compile")

# Test each combo
client_captures = {}  # server target, client target -> captured client output
server_captures = {}  # server target -> captured server output
for server_target, server_cmd, _, server_pattern, server_nocmp in targets:
    with capture_bg(server_cmd, nocmp=server_nocmp) as server_bg:
        server_bg.child.expect(server_pattern)  # Wait for "Blah HelloRPC server starting"
        for client_target, _, client_cmd, client_pattern, client_nocmp in targets:
            key = server_target, client_target
            suffix = " # " + server_target if server_target != client_target else ""
            client_captures[key] = capture(client_cmd + suffix, nocmp=client_nocmp)
            assert "Responding to [Hello from %s!] from %s" % (client_pattern, server_pattern) in \
                   client_captures[key].output
    server_captures[server_target] = server_bg.get_captured()
