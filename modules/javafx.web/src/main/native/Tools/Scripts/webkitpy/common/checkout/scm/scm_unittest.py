# Copyright (C) 2009, 2016 Apple Inc. All rights reserved.
from webkitpy.common.net.bugzilla import Attachment  # FIXME: This should not be needed

    process.communicate()  # ignore output
        self.dev_null = open(os.devnull, "w")  # Used to make our Popen calls quiet.
        input_process = subprocess.Popen(['echo', 'foo\nbar'], stdout=subprocess.PIPE, stderr=self.dev_null)  # grep shows usage and calls exit(2) when called w/o arguments.
        git_failure_message = "Merge conflict during commit: Your file or directory 'WebCore/ChangeLog' is probably out-of-date: resource out of date; try updating at /usr/local/libexec/git-core//git-svn line 469"
        svn_failure_message = """svn: Commit failed (details follow):
        self.assertItemsEqual(self.scm.revisions_changing_file("non_existent_file"), [])
        write_into_file_at_path(create_patch_path, '#!/bin/sh\necho $PWD')  # We could pass -n to prevent the \n, but not all echo accept -n.
        actual_patch_contents = scm.create_patch()
        expected_patch_contents = """Index: test_dir2/test_file2
===================================================================
--- test_dir2/test_file2\t(nonexistent)
+++ test_dir2/test_file2\t(working copy)
@@ -0,0 +1 @@\n+test content
\\ No newline at end of file
"""
        self.assertEqual(expected_patch_contents, actual_patch_contents)

        self.assertRaises(ScriptError, run_silent, ['git', 'svn', '--quiet', 'rebase'])  # Will fail due to a conflict leaving us mid-rebase.