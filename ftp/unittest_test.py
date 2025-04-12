import unittest
import sys
import os
import glob

# 테스트 파일이 있는 디렉토리를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_all_tests():
    """/test/ftp 디렉토리의 모든 테스트 파일 실행"""
    # 테스트 디렉토리 경로
    test_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'test',
        'ftp'
    )
    
    # 테스트 디렉토리가 존재하는지 확인
    if not os.path.exists(test_dir):
        print(f"Error: Test directory {test_dir} not found!")
        return False
        
    # 모든 테스트 파일 찾기
    test_files = glob.glob(os.path.join(test_dir, 'test*.py'))
    
    if not test_files:
        print(f"No test files found in {test_dir}")
        return False
        
    print(f"Found {len(test_files)} test files:")
    for test_file in test_files:
        print(f"  - {os.path.basename(test_file)}")
    
    # 모든 테스트 실행
    try:
        # 테스트 로더 생성
        loader = unittest.TestLoader()
        
        # 모든 테스트 파일에서 테스트 찾기
        suite = unittest.TestSuite()
        for test_file in test_files:
            # Python 3.5+ 스타일의 임포트
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                os.path.basename(test_file)[:-3],  # .py 확장자 제거
                test_file
            )
            test_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(test_module)
            
            # 모듈에서 모든 테스트 케이스 찾기
            module_suite = loader.loadTestsFromModule(test_module)
            suite.addTest(module_suite)
        
        # 테스트 실행
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        return result.wasSuccessful()
        
    except Exception as e:
        print(f"Error running tests: {str(e)}")
        return False

if __name__ == '__main__':
    # 모든 테스트 실행
    success = run_all_tests()
    
    # 결과에 따른 종료 코드 반환
    sys.exit(0 if success else 1) 